#!/usr/bin/env python3
"""Verify pinned historical bytes and declared initial KPS 12 transformations."""
from pathlib import Path
from kps12 import digest, dump, load, read_json
from migrate_kps12 import rewrite_body


def check(root):
    manifest=read_json(root/'migration/manifest.json')
    records,_=load(root)
    errors=[]
    for path,sha in manifest['baseline_files'].items():
        p=root/'legacy/kps9'/path
        if not p.is_file() or digest(p.read_bytes())!=sha:
            errors.append('Historical baseline changed: '+path)
    for item in manifest['migrated']:
        p=root/'legacy/kps9'/item['old_path']
        if not p.is_file():
            continue
        expected=rewrite_body(p.read_text(encoding='utf-8'),item['old_path'],manifest['path_map'])
        if digest(expected)!=item['canonical_body_sha256']:
            errors.append('Recorded transform does not reproduce: '+item['old_path'])
        r=records.get(item['id'])
        if r is None or r['migration']['old_id'] not in r['aliases']:
            errors.append('Lost migrated identity: '+item['id'])
        elif r['version']==item['initial_version']:
            if digest((root/r['content']).read_bytes())!=item['canonical_body_sha256']:
                errors.append('Initial-version content changed without versioning: '+item['id'])
    return {'ok':not errors,'baseline_files':len(manifest['baseline_files']),
            'migrated_records':len(manifest['migrated']),'errors':errors}

if __name__=='__main__':
    result=check(Path(__file__).resolve().parents[1]);print(dump(result));raise SystemExit(not result['ok'])
