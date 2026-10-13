#!/usr/bin/env python3
"""Build optional summary catalogs from Markdown; never rewrite knowledge or fingerprints."""
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
                index += f'**[{title}]({path}).** {summary}\n\n'
    index += '## Reading boundaries\n\nSubsystem and interface Models are self-contained explanations, not filtered link lists. Role and domain do not determine a compulsory reading order.\n'
    coverage = opening('Foundation coverage', 'Ten subsystem Models explain internal structure and major interfaces without claiming exhaustive coverage.')
    coverage += '\n## Domain entry points\n\n| Domain | Local summary | Model |\n|---|---|---|\n'
    for path, title, meta, summary in docs:
        if meta.get('system_domain'):
            coverage += f'| {meta["system_domain"]} | {summary.replace("|", ";")} | [{title}]({path}) |\n'
    coverage += ('\n## Interfaces\n\nAn interface Model specifies two analytical representations, a scoped relationship, a worked contrast and limits. '
                 'Fourteen Models cover selected links among the ten domains; this does not imply that every pair is connected or that the arrows are causal processing stages. '
                 'The subsystem Models explain these connections inline.\n\n'
                 '## Deliberate limits\n\nThe foundation does not exhaust accent inventories, acoustic measurement, lexical exceptions, formal derivations, '
                 'corpus frequencies, discourse frameworks, variation, acquisition or historical change. A topic being named or linked does not establish scientific adequacy. '
                 'Claim-specific external support and independent review remain incomplete.\n\n'
                 '## One complete case\n\n[One passage across ten domains](models/one-passage-ten-domains.md) separates the word forms, clause functions, participant roles, '
                 'reference choices, focus alternatives and predicted sound patterns of one constructed passage. No audio means no measured phonetic result.\n')
    queue = opening('Scientific review queue', 'Review evidence and scope rather than promoting claims because files or tests exist.')
    queue += ('\n## Review operation\n\nFor an item below, identify a bounded claim, inspect the relevant source passage, compare its scope with the local explanation, '
              'check a counterexample and record what remains unsupported. A citation is not blanket support, and a constructed example is not a study. '
              'Do not change scientific review status without an actual version-specific review record.\n\n'
              '## Pending items\n\n| Object | Claim or purpose to inspect | Current source boundary |\n|---|---|---|\n')
    for path, title, meta, summary in docs:
        boundary = 'Selected references only; inspect claim fit' if meta.get('references') else 'External support still pending'
        queue += f'| [{title}]({path}) | {summary.replace("|", ";")} | {boundary} |\n'
    return {'INDEX.md': index, 'COVERAGE.md': coverage, 'REVIEW-QUEUE.md': queue}

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
            path.write_text(content, encoding='utf-8')
    if stale:
        print('Stale catalogs: ' + ', '.join(stale))
        return 1
    print('Summary catalogs checked' if args.check else 'Summary catalogs written')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
