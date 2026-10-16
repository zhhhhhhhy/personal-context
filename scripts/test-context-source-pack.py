"""Focused guards for lossless sparse Observer input, without private fixtures."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('source_pack', Path(__file__).with_name('context-review.py'))
pack = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pack)


class SourcePackTests(unittest.TestCase):
    def test_url_login_token_is_redacted_without_losing_query_boundaries(self):
        spec = importlib.util.spec_from_file_location('extract', Path(__file__).with_name('extract-conversation-evidence.py'))
        extract = importlib.util.module_from_spec(spec); spec.loader.exec_module(extract)
        source = '查看https://example.test/wiki/doc?from=recent&disposable_login_token=FAKE_SECRET%3D.sig&next=ok#section 文档'
        redacted, count = extract.redact(source)
        self.assertNotIn('FAKE_SECRET', redacted)
        self.assertEqual(count, 1)
        self.assertIn('from=recent&disposable_login_token=[REDACTED_TOKEN]&next=ok#section 文档', redacted)

    def test_text_identity_shared_metadata_and_oversize_rejection(self):
        original = ['  中文\n条件：不少于20；不改英文。\u2028', '另一个项目\n引用“不是当前权限”']
        mapping = {f'M{i:03}': {'thread_id': f'parent-{i}', 'family_id': f'family-{i}',
                              'category': 'test', 'text': text} for i, text in enumerate(original, 1)}
        whole, pages = pack.source_packets({'source_digest': 'frozen'}, mapping, 180)
        self.assertEqual([m['text'] for page in pages for m in page['messages']], original)
        for page in pages:
            self.assertLessEqual(pack.token_count(page), 180)
            for message in page['messages']:
                self.assertEqual(set(message), {'id', 'conversation', 'text'})
                self.assertIn(message['conversation'], page['conversations'])
        with self.assertRaisesRegex(ValueError, 'never truncate'):
            pack.source_packets({'source_digest': 'frozen'}, mapping, 10)

    def test_changed_page_is_rejected_before_delivery(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp); page = run/'review/source/page-001.json'
            pack.save(page, {'messages': []})
            pack.save(run/'review/source-map.json', {'mapping': 'frozen'})
            pack.save(run/'review/source-manifest.json', {'files': [{'file': 'review/source/page-001.json', 'sha256': pack.sha(page)}],
                                                        'source_map_sha256': pack.sha(run/'review/source-map.json'), 'source_digest': 'frozen'})
            pack.save(page, {'messages': ['tampered']})
            with self.assertRaisesRegex(ValueError, 'frozen source page'):
                pack.deliver(run, 'review/source/page-001.json', 'observer', 6500)


if __name__ == '__main__':
    unittest.main()
