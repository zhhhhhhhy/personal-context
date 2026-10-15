"""Focused review protocol checks; synthetic training data only, no history/eval reads."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('review', Path(__file__).with_name('context-review.py'))
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)
v2 = review.v2()


class ReviewV2(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.run = Path(self.temp.name) / 'run'
        self.run.mkdir()
        self.ids = [f'M{i:03}' for i in range(1, 31)]
        _, self.sentinel, remaining = review.select([{'id': mid, 'risk_reasons': ['high'] if mid == 'M001' else []} for mid in self.ids])
        self.bridge, self.causal, self.unrelated = remaining[:3]
        source_rows = []
        for i, mid in enumerate(self.ids):
            # No accidental v1 source triggers on the low-risk rows.
            text = '至少 3 次。' if i == 0 else f'Handle request {chr(65 + i % 26)}{chr(65 + i // 26)}.'
            source_rows.append({'thread_id': 'a' if i % 2 == 0 else 'b', 'messages': [{
                'source_kind': 'user_authored', 'text': text,
                'evidence': {'file': f'/synthetic/{i % 2}.jsonl', 'line': i + 1}}]})
        review.save(self.run / 'cohort.json', {'coverage_required': True})
        review.save(self.run / 'train.selection.json', [{'thread_id': k, 'family_id': k, 'category': 'synthetic'} for k in ('a', 'b')])
        (self.run / 'evidence.train.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in source_rows), encoding='utf-8')
        review.save(self.run / 'input_hashes.json', {k: review.sha(self.run / k) for k in ('cohort.json', 'train.selection.json', 'evidence.train.jsonl')})
        self.inv, self.mapping = review.compact_sources(self.run)
        self.ledger = {'schema_version': 'coverage/1', 'run_id': 'run', 'source_digest': self.inv['source_digest'],
                       'messages': [], 'observations': [], 'review': {'completeness_reviewed': True, 'method': 'Synthetic unit inventory.'}}
        for i, (mid, source) in enumerate(self.mapping.items(), 1):
            claim = ('Three artifacts because of a dependency.' if mid == self.bridge else
                     'The result depends on a dependency.' if mid == self.causal else
                     'Render a table.' if mid == self.unrelated else 'Retain the task request.')
            scope = 'Only task A; preserve the quoted identifier “甲”.' if i == 1 else 'The local source task.'
            self.ledger['messages'].append({'message_id': source['message_id'], 'units': [{
                'id': f'U{i}', 'quote': source['text'], 'kind': 'task_requirement', 'claim': claim,
                'reason': 'Direct synthetic request.', 'observation_ids': [f'O{i}']}]})
            self.ledger['observations'].append({'id': f'O{i}', 'claim': claim, 'scope': scope, 'source_units': [f'U{i}']})
        review.save(self.run / 'observations.json', self.ledger)

    def prepare(self):
        return v2.prepare(self.run, 350)

    def report(self, result, issues=(), name='report.json'):
        data = copy.deepcopy(result['report_template'])
        data['issues'] = list(issues)
        path = self.run / name
        review.save(path, data)
        return path

    def issue(self, mid, risk_class, quote=None):
        return {'message_id': mid, 'risk_class': risk_class, 'kind': 'partial',
                'quote': quote or self.mapping[mid]['text'], 'problem': 'A synthetic detail was lost.',
                'minimal_repair': 'Restore the synthetic detail in its original task scope.'}

    def test_exact_source_scope_roundtrip_and_shared_once(self):
        self.assertNotIn('actor', v2.risk_tags('我希望你改进这个结果。', [], []))
        self.assertIn('actor', v2.risk_tags('图片由我自己插入。', [], []))
        self.assertNotIn('fidelity', v2.risk_tags('Explain the next task.', [], []))
        result = self.prepare()
        self.assertFalse(result['whole_fallback'])
        catalog = review.read(self.run / 'review/catalog.json')
        self.assertEqual(len(catalog['scopes']), 2)
        for row, source in zip(catalog['rows'], self.mapping.values()):
            self.assertEqual(row['text'], source['text'])
            for obs in row['observations']:
                expected = next(o for o in self.ledger['observations'] if o['id'] == obs['id'])
                self.assertEqual(catalog['scopes'][obs['scope_ref']], expected['scope'])
                self.assertEqual(obs['claim'], expected['claim'])
        shared = [review.read(self.run / f) for f in result['shared_files']]
        self.assertEqual(sum('task' in page for page in shared), 1)
        self.assertEqual({k: v for p in shared for k, v in p.get('scopes', {}).items()}, catalog['scopes'])
        pages = [review.read(self.run / f) for f in result['page_files']]
        self.assertGreater(len(pages), 1)
        self.assertTrue(all('task' not in p and 'core' not in p and review.token_count(p) <= 900 for p in pages))
        self.assertEqual(review.module().validate_coverage(self.run, self.run / 'observations.json')['status'], 'passed')

    def test_exact_ids_quote_enums_and_report_identity(self):
        result = self.prepare()
        good = self.report(result, [self.issue('M001', 'quantity')])
        v2.validate_report(self.run, good, False)
        original = review.read(good)
        mutations = [lambda d: d['checked_ids'].pop(),
                     lambda d: d['checked_ids'].append(d['checked_ids'][0]),
                     lambda d: d['issues'][0].update(quote='a fabricated quote'),
                     lambda d: d['issues'][0].update(risk_class='invented'),
                     lambda d: d['issues'][0].update(kind='invented'),
                     lambda d: d.update(source_digest='wrong'),
                     lambda d: d.update(manifest_sha256='wrong')]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                data = copy.deepcopy(original)
                mutate(data)
                review.save(good, data)
                with self.assertRaises(ValueError):
                    v2.validate_report(self.run, good, False)

    def test_shared_scope_does_not_contaminate_message_risks(self):
        source = 'Continue the task.'
        claims = [{'claim': 'Continue the task.'}]
        plain = [{'claim': 'Continue the task.', 'scope': 'Local task.'}]
        shared = [{'claim': 'Continue the task.', 'scope': '保留原文、数量阈值、引用和人工审核；必须解释原因。'}]
        self.assertEqual(v2.risk_tags(source, claims, plain), v2.risk_tags(source, claims, shared))
        self.assertEqual(v2.risk_tags(source, claims, shared), [])
        self.assertIn('quantity', v2.risk_tags('至少 10 条。', claims, shared))
        self.assertIn('constraint', v2.risk_tags(source, [{'claim': '只能修改文字。'}], plain))
        self.assertIn('actor', v2.risk_tags('评估方式我不知道。', [], []))
        self.assertIn('actor', v2.risk_tags("I don't know the evaluation approach.", [], []))
        self.assertNotIn('actor', v2.risk_tags('我希望你改进这个结果。', [], []))

    def test_all_issues_route_selectively_and_new_classes_chain(self):
        result = self.prepare()
        initial_hash = review.sha(self.run / 'review/plan.json')
        # Trigger is high-risk, not sentinel; expansion must use all findings.
        first = v2.route(self.run, [self.report(result, [self.issue('M001', 'quantity')])])
        self.assertEqual(first['selected_ids'], [self.bridge])
        second = v2.route(self.run, [self.report(first, [self.issue(self.bridge, 'causality')], 'followup.json')])
        self.assertEqual(second['selected_ids'], [self.causal])
        final = v2.route(self.run, [self.report(second, [], 'followup2.json')])
        self.assertEqual(final['selected_ids'], [])
        self.assertNotIn(self.unrelated, first['selected_ids'] + second['selected_ids'])
        audit = v2.route(self.run, audit=True)
        self.assertGreaterEqual(len(audit['selected_ids']), 2)
        self.assertLessEqual(len(audit['selected_ids']), 4)
        checked = set(result['report_template']['checked_ids'] + first['selected_ids'] + second['selected_ids'])
        self.assertFalse(checked & set(audit['selected_ids']))
        self.assertEqual(review.sha(self.run / 'review/plan.json'), initial_hash)
        with self.assertRaises(ValueError):
            v2.route(self.run, audit=True)

    def test_other_requires_explicit_conversation_and_does_not_expand_all(self):
        result = self.prepare()
        issue = self.issue('M001', 'other')
        path = self.report(result, [issue])
        with self.assertRaisesRegex(ValueError, 'same-conversation'):
            v2.validate_report(self.run, path, False)
        issue['scope'] = {'conversation': 'T01'}
        selected = v2.route(self.run, [self.report(result, [issue])])
        rows = review.read(self.run / 'review/catalog.json')['rows']
        expected = {r['id'] for r in rows if r['conversation'] == 'T01'} - set(result['report_template']['checked_ids'])
        self.assertEqual(set(selected['selected_ids']), expected)
        self.assertTrue(any(r['conversation'] == 'T02' and r['id'] not in selected['selected_ids'] for r in rows))

    def test_semantic_class_without_trigger_clue_uses_typed_route(self):
        result = self.prepare()
        path = self.report(result, [self.issue('M001', 'causality')])
        receipt = v2.validate_report(self.run, path, False)
        self.assertEqual(receipt['unmatched_issue_clues'], [{'message_id': 'M001', 'risk_class': 'causality'}])
        followup = v2.route(self.run, [path])
        self.assertEqual(set(followup['selected_ids']), {self.bridge, self.causal})
        self.assertNotIn(self.unrelated, followup['selected_ids'])

    def test_short_target_corrections_are_reference_clues(self):
        self.assertIn('format_reference', v2.risk_tags('不是应该修改验收单吗？', [], []))
        self.assertIn('format_reference', v2.risk_tags('请更正目标文件。', [], []))
        self.assertIn('format_reference', v2.risk_tags('继续。', [{'claim': '纠正编辑对象。'}], []))
        self.assertNotIn('format_reference', v2.risk_tags('继续。', [], []))

    def test_shared_prerequisite_duplicate_read_and_pending_result(self):
        result = self.prepare()
        with self.assertRaisesRegex(ValueError, 'shared'):
            v2.deliver(self.run, result['page_files'][0], 'reviewer', 900)
        for file in result['shared_files'] + result['page_files']:
            v2.deliver(self.run, file, 'reviewer', 900)
        file = result['page_files'][0]
        with self.assertRaisesRegex(ValueError, 'duplicate read'):
            v2.deliver(self.run, file, 'reviewer', 900)
        v2.deliver(self.run, file, 'reviewer', 900, 'Repair inspection explicitly required.')
        with self.assertRaisesRegex(ValueError, 'pending review'):
            v2.route(self.run)
        self.assertEqual(v2.reads(self.run)[-1]['reread_reason'], 'Repair inspection explicitly required.')

    def test_frozen_page_manifest_source_and_observation_drift(self):
        result = self.prepare()
        for file in (result['page_files'][0], 'review/initial/manifest.json', 'evidence.train.jsonl', 'observations.json', 'review/plan.json'):
            with self.subTest(file=file):
                path = self.run / file
                original = path.read_bytes()
                path.write_bytes(original + b' ')
                with self.assertRaises(ValueError):
                    v2.deliver(self.run, result['page_files'][0], 'reviewer', 900)
                path.write_bytes(original)

    def test_legacy_plan_result_and_read_remain_usable(self):
        with contextlib.redirect_stdout(io.StringIO()):
            review.prepare_review(self.run, protocol='v1')
        plan = review.read(self.run / 'review/plan.json')
        self.assertEqual(plan['version'], 'risk-review/1')
        report = {'messages': [{'id': mid, 'useful_requirements': 1, 'covered': 1, 'partial': 0, 'missing': 0, 'issues': []} for mid in plan['targeted_ids']]}
        review.save(self.run / 'legacy.json', report)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            review.check_review(self.run, self.run / 'legacy.json')
            review.deliver(self.run, 'review/targeted.json', 'legacy', 9000)
        self.assertIn('Handle request', output.getvalue())
        self.assertFalse(review.read(self.run / 'review/escalation.json')['remaining_review_required'])


if __name__ == '__main__':
    unittest.main()
