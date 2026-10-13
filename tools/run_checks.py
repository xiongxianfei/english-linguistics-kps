#!/usr/bin/env python3
"""Run actual package checks and write an input-hashed execution report.

The report is not an input to validation, a signature, or scientific approval.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from kps12 import dump, load, validate
from migrate_kps12 import migrate


def inventory(root: Path) -> dict[str, str]:
    result = {}
    for p in sorted(root.rglob('*')):
        relative = p.relative_to(root)
        if not p.is_file() or any(x in {'.git', '__pycache__'} for x in relative.parts) or p.suffix == '.pyc':
            continue
        if relative.as_posix() == 'validation-evidence.json':
            continue
        result[relative.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def reproduce(root: Path) -> dict:
    with tempfile.TemporaryDirectory(prefix='kps12-reproduce-') as tmp:
        target = Path(tmp) / 'rebuilt'
        migrate(root / 'legacy/kps9', target, assets=root)
        expected, actual = inventory(target), inventory(root)
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        changed = sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k])
        if missing or extra or changed:
            raise ValueError(dump({'missing': missing, 'extra': extra, 'changed': changed}))
        return {'ok': True, 'files_compared': len(expected), 'scope': 'Pinned first-migration reproduction, excluding runtime caches and this report.'}


def run(root: Path) -> int:
    root = root.resolve()
    before = inventory(root)
    specs = [
        ('KPS 12 structure', '.', ['validate.py', '.']),
        ('KPS 12 domain invariants', '.', ['tools/check_domain.py']),
        ('KPS 12 generated freshness', '.', ['tools/build_navigation.py', '--check']),
        ('Migration preservation', '.', ['tools/check_preservation.py']),
        ('KPS 12 regression tests', '.', ['-m', 'unittest', 'discover', '-s', 'tests', '-v']),
        ('KPS 9 historical structure', 'legacy/kps9', ['validate.py', '.']),
        ('KPS 9 historical upstream tests', 'legacy/kps9', ['test_validate.py']),
        ('KPS 9 historical domain invariants', 'legacy/kps9', ['tools/check_domain.py']),
        ('KPS 9 historical generated freshness', 'legacy/kps9', ['tools/build_navigation.py', '--check']),
        ('KPS 9 historical domain tests', 'legacy/kps9', ['-m', 'unittest', 'discover', '-s', 'tests', '-v']),
    ]
    checks = []
    for name, directory, args in specs:
        print('Checking: ' + name, flush=True)
        try:
            proc = subprocess.run([sys.executable, *args], cwd=root / directory,
                                  capture_output=True, text=True, timeout=180)
            output = proc.stdout + proc.stderr
            counts = re.findall(r'Ran (\d+) tests? in', output)
            item = {'name': name, 'cwd': directory, 'command': ['python3', *args],
                    'returncode': proc.returncode, 'ok': proc.returncode == 0,
                    'output_sha256': hashlib.sha256(output.encode()).hexdigest(),
                    'tests_run': int(counts[-1]) if counts else None, 'output': output}
        except subprocess.TimeoutExpired as exc:
            item = {'name': name, 'cwd': directory, 'command': ['python3', *args],
                    'ok': False, 'error': 'Timeout after 180 seconds; check did not complete.'}
        checks.append(item)
    try:
        checks.append({'name': 'Deterministic migration reproduction', **reproduce(root)})
    except (ValueError, OSError, KeyError) as exc:
        checks.append({'name': 'Deterministic migration reproduction', 'ok': False, 'error': str(exc)})
    after = inventory(root)
    checks.append({'name': 'Checks do not mutate payload', 'ok': before == after})
    result = validate(root)
    report = {'format': 12, 'kps_language': '12.x', 'profile_version': '12.0.0-draft.1',
              'executed_at': datetime.now(timezone.utc).isoformat(),
              'python': platform.python_version(), 'platform': platform.platform(),
              'baseline_commit': '034f21daa6946b744b367515cb4dbfc6a6720c4f',
              'scope': 'Executed structural and regression checks only; no scientific certification.',
              'independent_scientific_review': False, 'stats': result.get('stats', {}),
              'input_manifest_sha256': hashlib.sha256(dump(before).encode()).hexdigest(),
              'input_files_sha256': before, 'checks': checks,
              'ok': all(x['ok'] for x in checks) and result['ok']}
    (root / 'validation-evidence.json').write_text(dump(report), encoding='utf-8')
    print(dump({'ok': report['ok'], 'checks': len(checks), 'stats': report['stats'],
                'test_counts': {x['name']: x['tests_run'] for x in checks if x.get('tests_run')},
                'failed': [x['name'] for x in checks if not x['ok']]}))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=ROOT)
    p.add_argument('--reproduce-only', action='store_true')
    args = p.parse_args()
    if args.reproduce_only:
        try:
            print(dump(reproduce(args.root.resolve())))
        except (ValueError, OSError, KeyError) as exc:
            p.exit(1, str(exc) + '\n')
    else:
        raise SystemExit(run(args.root))
