"""Check canonical Context entry budgets without loading reference bodies."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def audit(root: Path, config: dict) -> dict:
    if config.get('schema_version') != 1 or not config.get('rules'):
        raise ValueError('budget config requires schema_version=1 and nonempty rules')
    if config.get('tokenizer') != 'o200k_base':
        raise ValueError('use the declared o200k_base measurement protocol')
    try:
        import tiktoken
    except ImportError as exc:
        raise ValueError('tiktoken is required; no character-count fallback is used') from exc
    encoding = tiktoken.get_encoding('o200k_base')
    results = []
    for rule in config['rules']:
        name = rule['name']
        if ('paths' in rule) == ('glob' in rule):
            raise ValueError(f'{name}: select either paths or glob')
        if ('max_tokens' in rule) == ('max_tokens_per_file' in rule):
            raise ValueError(f'{name}: specify one group or per-file limit')
        per_file = 'max_tokens_per_file' in rule
        limit = rule['max_tokens_per_file' if per_file else 'max_tokens']
        if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
            raise ValueError(f'{name}: limit must be a positive integer')
        paths = sorted(root.glob(rule['glob'])) if 'glob' in rule else [root / value for value in rule['paths']]
        files = []
        errors = []
        if not paths:
            errors.append('no matching entry files')
        for path in paths:
            path = path.resolve()
            if not path.is_relative_to(root):
                raise ValueError(f'{name}: entry escapes repository root')
            relative = path.relative_to(root).as_posix()
            if not path.is_file():
                errors.append(f'missing entry: {relative}')
                continue
            text = path.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
            tokens = len(encoding.encode(text, disallowed_special=()))
            files.append({'path': relative, 'tokens': tokens, 'chars': len(text)})
            if per_file and tokens > limit:
                errors.append(f'over budget: {relative} ({tokens} > {limit})')
        total = sum(item['tokens'] for item in files)
        if not per_file and total > limit:
            errors.append(f'over budget: {name} ({total} > {limit})')
        results.append({'name': name, 'mode': 'per_file' if per_file else 'group', 'limit': limit, 'tokens': total, 'files': files, 'errors': errors, 'status': 'passed' if not errors else 'rejected'})
    return {'schema_version': 1, 'tokenizer': 'o200k_base', 'measurement': 'UTF-8 text with LF line endings; file bodies only, not live session usage', 'status': 'passed' if all(item['status'] == 'passed' for item in results) else 'rejected', 'rules': results}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--config', type=Path, default=Path('docs/context-loading/budgets.json'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    config_path = args.config if args.config.is_absolute() else root / args.config
    try:
        result = audit(root, json.loads(config_path.read_text(encoding='utf-8')))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        result = {'status': 'rejected', 'errors': [str(exc)]}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    summary = {key: value for key, value in result.items() if key != 'rules'}
    if 'rules' in result:
        summary['rules'] = [{key: value for key, value in item.items() if key != 'files'} for item in result['rules']]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['status'] == 'passed' else 2)


if __name__ == '__main__':
    main()
