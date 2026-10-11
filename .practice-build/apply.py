"""One-time verified application of authored Practice files; no content generation or networking."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import lzma
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = 'd0c0874d920be1acc34fe266e94acad6ef4c67fd'
PAYLOAD_SHA = '1ebef99c1e8f7aa05b22223a4722b1af5379c1afdfe3edc3123ea3f9e795f5f3'
AUTHORED = {
    'CHANGELOG.md', 'CHECKS.md', 'PRONUNCIATION.md', 'README.md', 'SCOPE.md',
    'data/pronunciation-practice-validation.json',
    'practices/classify-and-produce-phone.md', 'practices/learn-word-pronunciation.md',
    'references/README.md',
    'references/international-phonetic-association-undated-diacritics-and-other-symbols.md',
    'references/merriam-webster-undated-pin-entry.md',
    'tests/test_pronunciation_practices.py',
}
GENERATED = {'COVERAGE.md', 'INDEX.md', 'REVIEW-QUEUE.md',
             'knowledge-graph.json', 'summary-dependencies.json'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def location(name):
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or name not in AUTHORED | GENERATED:
        raise ValueError('Disallowed publication path: ' + name)
    target = ROOT.joinpath(*p.parts)
    if target.is_symlink():
        raise ValueError('Unexpected symlink: ' + name)
    target.resolve().relative_to(ROOT.resolve())
    return target

def run(args):
    print('$ ' + ' '.join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)

def main():
    os.chdir(ROOT)
    raw = b''.join((ROOT / '.practice-build' / ('payload%d.bin' % i)).read_bytes() for i in range(4))
    if digest(raw) != PAYLOAD_SHA:
        raise ValueError('Payload hash mismatch')
    decoded = lzma.decompress(raw, memlimit=128 * 1024 * 1024)
    if len(decoded) > 2 * 1024 * 1024:
        raise ValueError('Unexpected payload size')
    package = json.loads(decoded)
    if package['format'] != 1 or package['base_commit'] != BASE:
        raise ValueError('Unexpected payload format or base')
    entries = package['files']
    if len(entries) != len(AUTHORED) or {e['path'] for e in entries} != AUTHORED:
        raise ValueError('Unexpected authored file inventory')
    if set(package['generated']) != GENERATED:
        raise ValueError('Unexpected generated inventory')
    prepared = []
    for entry in entries:
        target = location(entry['path'])
        before = digest(target.read_bytes()) if target.exists() else None
        if before != entry['before']:
            raise ValueError('Base file changed: ' + entry['path'])
        content = entry['content'].encode('utf-8')
        if digest(content) != entry['sha256']:
            raise ValueError('Authored content hash mismatch: ' + entry['path'])
        prepared.append((target, content))
    for target, content in prepared:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    print('Applied %d preflight-verified authored files' % len(prepared), flush=True)
    run([sys.executable, 'tools/build_navigation.py'])
    sys.path.insert(0, str(ROOT))
    import validate as kps
    docs, byid = {}, {}
    for path in sorted(ROOT.rglob('*.md')):
        if '.github' in path.relative_to(ROOT).parts:
            continue
        doc = kps.parse(path)
        docs[path] = doc
        if doc.meta.get('id'):
            byid[doc.meta['id']] = doc
    snapshot = json.dumps(kps.snapshot(ROOT, docs, byid), ensure_ascii=False, indent=2) + '\n'
    expected = package['generated']['summary-dependencies.json']
    if digest(snapshot.encode('utf-8')) != expected:
        raise ValueError('Snapshot differs from pre-reviewed local baseline')
    location('summary-dependencies.json').write_bytes(snapshot.encode('utf-8'))
    for name, expected in package['generated'].items():
        if digest(location(name).read_bytes()) != expected:
            raise ValueError('Generated file differs from reviewed local result: ' + name)
    for entry in entries:
        if digest(location(entry['path']).read_bytes()) != entry['sha256']:
            raise ValueError('Unexpected post-application modification: ' + entry['path'])
    commands = [
        [sys.executable, 'validate.py', '.'],
        [sys.executable, 'test_validate.py'],
        [sys.executable, 'tools/check_domain.py'],
        [sys.executable, 'tools/build_navigation.py', '--check'],
        [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
    ]
    for args in commands:
        run(args)
    print('All checks passed on exact reviewed content; no scientific review or learner outcome claimed.', flush=True)

if __name__ == '__main__':
    main()
