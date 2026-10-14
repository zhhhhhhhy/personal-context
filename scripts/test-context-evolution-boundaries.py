"""Focused privacy/provenance regressions; all mutations use a temporary repo."""
import argparse
import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(filename))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


evolution = module('evolution', 'context-evolution.py')
extractor = module('extractor', 'extract-conversation-evidence.py')


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.temp.name)
        self.old_root = evolution.REPO_ROOT
        evolution.REPO_ROOT = self.root
        self.run = self.root / '.local/run'
        self.run.mkdir(parents=True)
        self.args = argparse.Namespace(run_dir=self.run)
        evolution.write_json(self.root/'habits/learned.json', {'items': []})
        evolution.write_text(self.root/'habits/learned.md', '# Learned\n')
        evolution.write_json(self.run/'base_snapshot.json', evolution.base_snapshot())
        evolution.write_json(self.run/'cohort.json', {'train_thread_ids':['a','b'], 'eval_thread_ids':['c']})
        evolution.write_json(self.run/'train.selection.json', [{'thread_id':x,'family_id':x} for x in ['a','b']])
        self.messages = [{'thread_id':x,'messages':[{'source_kind':'user_authored','text':text,'evidence':{'line':6,'file':x+'.jsonl'}}]} for x,text in [('a','First direct request'),('b','Second independent request')]]
        self.write_messages()
        self.reflection = {
            'schema_version':'0.1', 'run_id':'run',
            'base_snapshot_sha256':evolution.current_base_hash(),
            'conflict_check':dict(core_checked=True, learned_checked=True, candidate_ledger_checked=True),
            'promotions':[{'key':'test.example','claim':'Scoped example','scope':'Specific test task','confidence':'medium','sensitivity':'non_sensitive','exceptions':['Outside scope'],'candidate_audit':{'action':'new','related_ids':[]},'evidence':[{'thread_id':x,'source_kind':'user_authored','location':x+'.jsonl:L6','support':'Direct example'} for x in ['a','b']]}],
            'deferred':[], 'rejected':[]}
        self.write_reflection()

    def tearDown(self):
        evolution.REPO_ROOT = self.old_root
        self.temp.cleanup()

    def write_messages(self):
        evolution.write_text(self.run/'evidence.train.jsonl', ''.join(json.dumps(x)+'\n' for x in self.messages))

    def write_reflection(self):
        evolution.write_json(self.run/'reflection.json', self.reflection)

    def test_wrappers_plans_and_ide_duplicates(self):
        texts = ['# AGENTS.md instructions for /example', 'PLEASE IMPLEMENT THIS PLAN:\nAn assistant plan', 'A direct request', '# Context from my IDE setup:\n## My request for Codex:\nA direct request']
        path = self.root/'source.jsonl'
        records = [{'type':'response_item','timestamp':'2026-10-01T00:00:00Z','payload':{'type':'message','role':'user','content':text}} for text in texts]
        path.write_text(''.join(json.dumps(x)+'\n' for x in records), encoding='utf-8')
        data = extractor.collect_thread({'thread_id':'a','session_files':[{'path':str(path)}]}, [], self.root, 6000)
        self.assertEqual([x['source_kind'] for x in data['messages']], ['user_plan_confirmation','user_authored'])
        self.assertEqual(data['messages'][1]['text'], 'A direct request')

    def test_stratified_selection_rejects_family_leak(self):
        index=self.root/'index.jsonl'
        index.write_text(''.join(json.dumps({'thread_id':x,'kind':'root_conversation','created_at':'2026-10-01'})+'\n' for x in ['a','b']), encoding='utf-8')
        manifest=self.root/'partition.json'
        evolution.write_json(manifest,[{'thread_id':'a','category':'research','family_id':'same','partition':'train'},{'thread_id':'b','category':'research','family_id':'same','partition':'eval'}])
        args=argparse.Namespace(index=index,output=self.root/'prepared',exclude_selection=[],start='2026-10-01',end='2026-10-02',partition_manifest=manifest,eval_count=1)
        with self.assertRaisesRegex(SystemExit,'family crosses'):
            evolution.cmd_prepare(args)
        self.assertFalse(args.output.exists())

    def test_frozen_input_tamper_rejected(self):
        evolution.write_json(self.run/'input_hashes.json',{'evidence.train.jsonl':evolution.sha256_file(self.run/'evidence.train.jsonl')})
        self.messages[0]['messages'][0]['text']='Rewritten evidence'
        self.write_messages()
        self.assertIn('prepared input changed', ' '.join(evolution.validate_reflection(self.run)['errors']))

    def test_duplicate_expression_and_family_do_not_count_twice(self):
        self.messages[1]['messages'][0]['text']=self.messages[0]['messages'][0]['text']
        self.write_messages()
        self.assertEqual(evolution.validate_reflection(self.run)['status'],'rejected')
        self.messages[1]['messages'][0]['text']='Different wording'
        self.write_messages()
        evolution.write_json(self.run/'train.selection.json',[{'thread_id':x,'family_id':'same'} for x in ['a','b']])
        self.assertEqual(evolution.validate_reflection(self.run)['status'],'rejected')

    def test_fabricated_filename_and_plan_source_rejected(self):
        self.reflection['promotions'][0]['evidence'][0]['location']='invented.jsonl:L6'
        self.write_reflection()
        self.assertIn('filename', ' '.join(evolution.validate_reflection(self.run)['errors']))
        self.reflection['promotions'][0]['evidence'][0]['location']='a.jsonl:L6'
        self.messages[0]['messages'][0]['source_kind']='user_plan_confirmation'
        self.write_messages()
        self.write_reflection()
        self.assertEqual(evolution.validate_reflection(self.run)['status'],'rejected')

    def test_apply_revalidates_modified_reflection(self):
        evolution.write_json(self.run/'validation.json', evolution.validate_reflection(self.run))
        before=(self.root/'habits/learned.json').read_bytes()
        self.reflection['promotions'][0]['sensitivity']='local_only'
        self.write_reflection()
        with self.assertRaisesRegex(SystemExit,'changed after validation'):
            evolution.cmd_apply(self.args)
        self.assertEqual((self.root/'habits/learned.json').read_bytes(),before)
        self.reflection['promotions'][0]['sensitivity']='non_sensitive'
        for field in ('reinforced','deferred','rejected'):
            with self.subTest(field=field):
                self.reflection[field]=[{'claim':'Missing reason'}]
                self.write_reflection()
                with self.assertRaisesRegex(SystemExit,'changed after validation'):
                    evolution.cmd_apply(self.args)
                self.assertEqual((self.root/'habits/learned.json').read_bytes(),before)
                del self.reflection[field]

    def test_apply_and_rollback_preserve_base(self):
        before=evolution.current_base_hash()
        evolution.write_json(self.run/'validation.json', evolution.validate_reflection(self.run))
        with contextlib.redirect_stdout(io.StringIO()):
            evolution.cmd_apply(self.args)
            self.assertEqual(evolution.load_json(self.root/'habits/learned.json')['items'][0]['key'],'test.example')
            evolution.cmd_rollback(self.args)
        self.assertEqual(evolution.current_base_hash(),before)


if __name__ == '__main__':
    unittest.main()
