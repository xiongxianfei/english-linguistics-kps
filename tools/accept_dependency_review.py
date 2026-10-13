#!/usr/bin/env python3
"""Record an explicitly supplied editorial review; never infer scientific approval."""
import argparse
from pathlib import Path
from kps12 import current_dependencies, digest, dump, load, read_json, safe_path


def accept(root, record_path):
    record_path = Path(record_path).resolve()
    if not record_path.is_relative_to(root.resolve()):
        raise ValueError('review record must be committed inside the package')
    review = read_json(record_path)
    previous = read_json(root / 'summary-dependencies.json')
    records, _ = load(root)
    current = current_dependencies(root, records)
    old_hashes, new_hashes = previous['content_sha256'], current['content_sha256']
    changed = {i for i in set(old_hashes) | set(new_hashes) if old_hashes.get(i) != new_hashes.get(i)}
    changed |= {i for i in set(previous['dependencies']) | set(current['dependencies'])
                if previous['dependencies'].get(i) != current['dependencies'].get(i)}
    affected = {i for dependencies in (previous['dependencies'], current['dependencies'])
                for i, deps in dependencies.items() if changed.intersection(deps)}
    if not changed:
        raise ValueError('no dependency changes to accept')
    for key in ('reviewer', 'date', 'findings'):
        if not isinstance(review.get(key), str) or not review[key].strip():
            raise ValueError('missing editorial declaration: ' + key)
    if review.get('before_sha256') != digest(dump(previous)) or review.get('after_sha256') != digest(dump(current)):
        raise ValueError('review hashes do not match the actual before/after snapshots')
    if set(review.get('changed_entities', [])) != changed or set(review.get('affected_dependents', [])) != affected:
        raise ValueError('review does not cover the exact changed entities and affected dependents')
    (root / 'summary-dependencies.json').write_text(dump(current), encoding='utf-8')
    return {'changed_entities': sorted(changed), 'affected_dependents': sorted(affected),
            'scientific_status_changed': False}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record', type=Path, required=True)
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        print(dump(accept(root, args.record)))
    except (ValueError, OSError, KeyError) as exc:
        p.exit(1, str(exc) + '\n')
