"""Return and meter Context payloads for a controlled local evolution run.

This measures returned text, not platform prompts or total session usage. Logs
and payloads are restricted to the ignored local run directory.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = [
    'rules/SOUL.md', 'profile.md', 'habits/communication.md', 'INDEX.md',
    'AGENTS.md', 'skills/personal-context/SKILL.md', 'rules/CONTEXT_LOADING.md',
    'docs/evolution/POLICY.md', 'references/skills/personal-context-evolution.md',
    'habits/learned.md',
]


def evolution():
    spec = importlib.util.spec_from_file_location('context_evolution', ROOT / 'scripts/context-evolution.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def coverage():
    spec = importlib.util.spec_from_file_location('context_coverage', ROOT / 'scripts/context-coverage.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def scrub(text: str) -> str:
    text = re.sub(r'(?:gh[pousr]_|github_pat_|sk-)[A-Za-z0-9_-]{12,}', '[REDACTED]', text)
    text = re.sub(r'(?i)((?:password|passwd|api[_-]?key|access[_-]?token|authorization)\s*[:=：]\s*)[^\s,;；]+', r'\1[REDACTED]', text)
    return re.sub(r'(密码\s*(?:[:=：]\s*)?)[A-Za-z0-9][^\s，。；;]{2,}', r'\1[REDACTED]', text)


def scrub_data(value):
    # Redact string values before serialization so quote characters in a match
    # cannot consume JSON delimiters and invalidate the returned payload.
    if isinstance(value, str):
        return scrub(value)
    if isinstance(value, list):
        return [scrub_data(item) for item in value]
    if isinstance(value, dict):
        return {key: scrub_data(item) for key, item in value.items()}
    return value


def candidate_data(module):
    return [module.lookup_candidate(key) for key in sorted(module.candidate_ids())]


def main():
    import tiktoken
    # Native Windows Python may inherit a legacy console encoding. Return the
    # same UTF-8/LF bytes we persist and meter, even without python -X utf8.
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    parser.add_argument('--arm', choices=['progressive', 'whole', 'parent', 'regression', 'reference'], required=True)
    parser.add_argument('--max-tokens', type=int, default=9000)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('bootstrap')
    train = sub.add_parser('train')
    train.add_argument('--offset', type=int, default=0)
    train.add_argument('--limit', type=int, default=24)
    sub.add_parser('whole-candidates')
    file = sub.add_parser('file')
    file.add_argument('--path', required=True)
    file.add_argument('--heading')
    candidate = sub.add_parser('candidate')
    candidate.add_argument('--id', required=True)
    search = sub.add_parser('search')
    search.add_argument('--terms', required=True, help='regular expression over claim and scope')
    search.add_argument('--limit', type=int, default=8)
    args = parser.parse_args()
    run = args.run_dir.resolve()
    if not run.is_relative_to((ROOT / '.local/context-evolution').resolve()) or not (run / 'cohort.json').is_file():
        raise SystemExit('run must be a prepared, ignored local evolution directory')
    module = evolution()
    if args.command == 'bootstrap':
        data = [{'file': name, 'text': (ROOT / name).read_text(encoding='utf-8-sig')} for name in BOOTSTRAP]
    elif args.command == 'train':
        if args.offset < 0 or args.limit < 1:
            raise SystemExit('train requires a nonnegative offset and a positive limit')
        inventory = coverage().source_inventory(run)
        rows = inventory['messages']
        selected = rows[args.offset:args.offset + args.limit]
        threads = {}
        for row in selected:
            thread = threads.setdefault(row['thread_id'], {key: row[key] for key in ('thread_id', 'category', 'family_id')})
            thread.setdefault('messages', []).append({key: row[key] for key in ('message_id', 'location', 'truncated', 'text')})
        end = args.offset + len(selected)
        data = {'source_digest': inventory['source_digest'], 'total_messages': len(rows), 'offset': args.offset, 'returned_messages': len(selected), 'next_offset': end if end < len(rows) else None, 'threads': list(threads.values())}
    elif args.command == 'candidate':
        data = module.lookup_candidate(args.id)
    elif args.command == 'search':
        expression = re.compile(args.terms, re.I)
        matches = []
        for record in candidate_data(module):
            claim = re.search(r'^- claim: (.*)', record['text'], re.M)
            scope = re.search(r'^- scope: (.*)', record['text'], re.M)
            text = (claim.group(1) if claim else '') + '\n' + (scope.group(1) if scope else '')
            if expression.search(text):
                matches.append({'id': record['id'], 'claim': claim.group(1) if claim else '', 'scope': scope.group(1) if scope else ''})
        data = {'match_count': len(matches), 'shown': matches[:args.limit], 'more': len(matches) > args.limit}
    elif args.command == 'whole-candidates':
        if args.arm != 'whole':
            raise SystemExit('whole-candidates is reserved for the explicit comparison arm')
        text = subprocess.check_output(['git', 'show', 'ed1af97:notes/candidates.md'], cwd=ROOT).decode('utf-8')
        old = {key: body.strip() for key, body in re.findall(r'^## (C-\d{8}-\d{3})\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)}
        current = {row['id']: row['text'].split('\n', 1)[1].strip() for row in candidate_data(module)}
        if old != current:
            raise SystemExit('candidate records changed; archived ledger is not a matched-input baseline')
        data = {'source': 'git:ed1af97:notes/candidates.md', 'text': text}
    else:
        path = (ROOT / args.path).resolve()
        if not path.is_relative_to(ROOT) or path.is_relative_to(ROOT / '.local'):
            raise SystemExit('file reads must remain in canonical repository content')
        text = path.read_text(encoding='utf-8-sig')
        if args.heading:
            lines = text.splitlines()
            start = next((i for i, line in enumerate(lines) if line.strip() == args.heading), None)
            if start is None:
                raise SystemExit('requested heading not found')
            level = len(lines[start]) - len(lines[start].lstrip('#'))
            end = next((i for i in range(start + 1, len(lines)) if re.match(r'^#{1,' + str(level) + r'} ', lines[i])), len(lines))
            text = '\n'.join(lines[start:end]).rstrip()
        data = {'file': path.relative_to(ROOT).as_posix(), 'heading': args.heading, 'text': text}
    payload = json.dumps(scrub_data(data), ensure_ascii=False, indent=2) + '\n'
    count = len(tiktoken.get_encoding('o200k_base').encode(payload, disallowed_special=()))
    if count > args.max_tokens:
        raise SystemExit(f'payload {count} tokens exceeds return limit {args.max_tokens}; narrow the read')
    logdir = run / 'loads' / args.arm
    logdir.mkdir(parents=True, exist_ok=True)
    event_id = str(time.time_ns())
    payload_path = logdir / f'{event_id}.txt'
    payload_path.write_text(payload, encoding='utf-8', newline='\n')
    event = {'event_id': event_id, 'command': args.command, 'selector': {key: value for key, value in vars(args).items() if key not in {'run_dir', 'max_tokens', 'arm'}}, 'category': 'history' if args.command == 'train' else 'context', 'tokenizer': 'o200k_base', 'tokens': count, 'chars': len(payload), 'payload_sha256': hashlib.sha256(payload.encode('utf-8')).hexdigest(), 'payload_file': payload_path.name}
    with (logdir / 'reads.jsonl').open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + '\n')
    sys.stdout.write(payload)


if __name__ == '__main__':
    main()
