#!/usr/bin/env python3
"""Build the optional knowledge index from Markdown; never rewrite knowledge or fingerprints."""
import argparse
import pathlib
import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate as kps
ROLES = ['concept', 'principle', 'model', 'method', 'practice']

def opening(title, takeaway):
    return ('---\nlanguage: "KPS 9.x"\npackage_version: "0.2.0"\nstatus: "draft"\n---\n\n# ' + title +
            '\n\n## Key takeaway\n' + takeaway + '\n\n## Summary\nThis is an optional catalog of canonical Markdown, not another knowledge store. '
            'Each item has a local summary here; its full explanation, examples and limits remain in its owning file. '
            'All linguistic content is provisional.\n')

def collect():
    docs = []
    for role in ROLES:
        for path in sorted((ROOT / (role + 's')).glob('*.md')):
            doc = kps.parse(path)
            if doc.meta.get('type') == role:
                title = next(h for n, h in doc.headings if n == 1)
                summary = ' '.join(kps.section(doc, 'Key takeaway').split())
                docs.append((path.relative_to(ROOT).as_posix(), title, doc.meta, summary))
    return docs

def generated():
    docs = collect()
    index = opening('Knowledge index', 'Locate knowledge by its primary role and inspect the local explanation before applying it.')
    for role in ROLES:
        index += '\n## ' + role.capitalize() + 's\n\n'
        for path, title, meta, summary in docs:
            if meta['type'] == role:
                index += f'**[{title}](../{path}).** {summary}\n\n'
    index += '## Reading boundaries\n\nSubsystem and interface Models are self-contained explanations, not filtered link lists. Role and domain do not determine a compulsory reading order.\n'
    index+='\n## Review and scope\n\n[Review priorities](REVIEW.md#priority-evidence-gaps) explain the remaining evidence work. [One passage across ten domains](../models/one-passage-ten-domains.md) illustrates the integrated analysis; no audio means no measured phonetic result.\n'
    return {'docs/INDEX.md': index}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for name, content in generated().items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8') != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    if stale:
        print('Stale index: ' + ', '.join(stale))
        return 1
    print('Knowledge index checked' if args.check else 'Knowledge index written')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
