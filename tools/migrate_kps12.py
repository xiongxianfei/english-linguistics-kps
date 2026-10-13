#!/usr/bin/env python3
"""Deterministic, offline KPS 9 -> KPS 12 package migration.

Reads the exact pinned baseline and refuses a nonempty output directory.
The five legacy roles remain independent classifications, not structural kinds.
"""
from __future__ import annotations
import argparse
import ast
import json
import os
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kps12 import PROFILE, Document, current_dependencies, digest, dump, generated, load, section, slug, validate

BASE = '034f21daa6946b744b367515cb4dbfc6a6720c4f'
ROLE_NAMES = ['concept', 'principle', 'model', 'method', 'practice']
LEGACY_RELATIONS = {'uses_concepts': 'concept', 'uses_principles': 'principle',
                    'uses_models': 'model', 'uses_methods': 'method', 'uses_practices': 'practice',
                    'composes': 'practice', 'references': 'source', 'related_knowledge': None}
MAINTENANCE_NOTE = '''\n## KPS 12 migration note\n\nThe active root validator now checks the KPS 12 entity profile. The historical upstream KPS 9 validator remains under legacy/kps9 and is not the active language contract. Existing command entrypoints are retained. Dependency acceptance now requires an explicit editorial review record through tools/accept_dependency_review.py; a bare refresh flag is not supported. These operational clarifications do not establish scientific review.\n'''


def legacy_parts(text):
    if not text.startswith('---\n'):
        return {}, text
    stop = text.find('\n---\n', 4)
    if stop < 0:
        raise ValueError('unterminated legacy frontmatter')
    meta = {}
    for line in text[4:stop].splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        key, value = line.split(':', 1)
        if key in meta:
            raise ValueError('duplicate legacy metadata key')
        meta[key] = json.loads(value)
    return meta, text[stop + 5:].lstrip('\n')


def rewrite_body(text, old_path, path_map):
    _, body = legacy_parts(text)
    new_path = path_map.get(old_path, old_path)
    def rewrite(match):
        dest = match[2]
        p = urlsplit(dest)
        if p.scheme or p.netloc:
            return match[0]
        if not p.path:
            return match[0]
        resolved = os.path.normpath(os.path.join(os.path.dirname(old_path), p.path)).replace(os.sep, '/')
        target = path_map.get(resolved, resolved)
        relative = os.path.relpath(target, os.path.dirname(new_path) or '.').replace(os.sep, '/')
        return match[1] + urlunsplit(('', '', relative, p.query, p.fragment)) + ')'
    body = re.sub(r'(\[[^\]]+\]\()([^)]*)\)', rewrite, body)
    if old_path == 'practices/maintain-english-package.md':
        body = body.rstrip() + '\n' + MAINTENANCE_NOTE
    return body


def entity(ident, kind, label, **extra):
    return dict(schema='kps:12:entity', id=ident, kind=kind, label=label,
                version='0.1.0', status='draft', roles=[], domains=[], aliases=[], relations=[], **extra)


def record_filename(ident):
    return 'entities/' + ident.replace(':', '--') + '.json'


def write_record(root, record):
    path = root / record_filename(record['id'])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(record), encoding='utf-8')


def redirect(body, original_path, destination):
    doc = Document(Path(original_path), {}, legacy_parts(body)[1])
    title = next(h for level, h in doc.headings if level == 1)
    relative = os.path.relpath(destination, os.path.dirname(original_path) or '.').replace(os.sep, '/')
    result = f'# {title}\n\n'
    for level, heading in doc.headings:
        if level != 2:
            continue
        result += f'## {heading}\n\nThis is a compatibility redirect. Read [{heading}]({relative}#{slug(heading)}) in the canonical KPS 12 content.\n\n'
    return result


def add_ontology(records, plan):
    def add(r):
        if r['id'] in records:
            raise ValueError('identity collision: ' + r['id'])
        records[r['id']] = r
    sections = {
        'concept': ['Definition', 'Distinctions', 'Scope and limits'],
        'principle': ['Statement', 'Explanation', 'Scope and counterevidence'],
        'model': ['Purpose', 'Representation', 'Assumptions and limits', 'Evaluation and counterevidence'],
        'method': ['Objective', 'Inputs and prerequisites', 'Rationale', 'Procedure', 'Expected effect', 'Validation and counterevidence'],
        'practice': ['Purpose and prerequisites', 'Stage map', 'Current practice summary']}
    meanings = {
        'concept': 'Defines a locally reusable distinction.',
        'principle': 'States and explains a scoped relationship with counterevidence boundaries.',
        'model': 'Represents a system with assumptions, implications and limits.',
        'method': 'Supplies a bounded repeatable operation and validation criteria.',
        'practice': 'Composes locally executable operations toward a recurring goal.'}
    for role in ROLE_NAMES:
        add(entity('kps:role:' + role, 'role', role.capitalize(), description=meanings[role], required_sections=sections[role]))
    add(entity('linguistics:language', 'domain', 'Linguistics', parents=[], top_level=False,
               scope='Provisional subject-classification root for this English package, not a complete universal ontology.'))
    add(entity('linguistics:foundations', 'domain', 'Analytical foundations', parents=['linguistics:language'], top_level=False,
               scope='Cross-domain distinctions such as representation, category, function, constituency and acceptability.'))
    add(entity('kps:knowledge-maintenance', 'domain', 'Knowledge investigation and maintenance', parents=[], top_level=False,
               scope='Evidence evaluation, representation design and editorial maintenance; not a linguistic subsystem.'))
    for d in plan['domains']:
        add(entity('linguistics:' + d['slug'], 'domain', d['label'], parents=d['parents'], top_level=d['top_level'], scope=d['scope']))
    K = ['knowledge', 'interface']
    A = ['knowledge', 'interface', 'representation', 'source', 'domain', 'role', 'relation-type', 'claim', 'evidence', 'sequence']
    predicates = {
        'uses': (K, K, 'document', False, 'Document depends on another explanation; not a causal or learning prerequisite claim.'),
        'cites': (K, ['source'], 'document', False, 'Document links a source; support for a particular claim is not inferred.'),
        'composes': (K, K, 'workflow', True, 'Practice composes another Practice; both endpoints require the Practice role.'),
        'related-to': (K, K, 'navigation', False, 'Declared topical navigation link; no causal or automatic inverse inference.'),
        'maps-to': (['representation'], ['representation'], 'semantic', False, 'Scoped analytical correspondence; no temporal-processing or one-to-one claim.'),
        'constrains': (['representation'], ['representation'], 'semantic', False, 'A scoped representation constrains possible analyses of another; not sufficient determination.'),
        'realizes': (['representation'], ['representation'], 'semantic', False, 'A scoped realization correspondence, not an unqualified identity relation.'),
        'classified-as-role': (K, ['role'], 'classification', False, 'Independent functional role membership.'),
        'in-domain': (A, ['domain'], 'classification', False, 'Explicit subject membership, with overlaps permitted.'),
        'broader-domain': (['domain'], ['domain'], 'classification', True, 'Broader classification scope, not linguistic causation.'),
        'asserts': (K, ['claim'], 'claim', False, 'Ownership of a versioned authored claim.'),
        'in-sequence': (K, ['sequence'], 'navigation', False, 'Positions in a named navigation route, not ontological identity.'),
        'source-representation': (['interface'], ['representation'], 'interface', False, 'The source endpoint of a documented mapping.'),
        'target-representation': (['interface'], ['representation'], 'interface', False, 'The target endpoint of a documented mapping.'),
        'evidence-from': (['evidence'], ['source'], 'evidence', False, 'Source provenance of an evidence assessment.'),
        'evidence-about': (['evidence'], K + ['claim'], 'evidence', False, 'Target of a contextual or claim-level evidence assessment.')}
    for name, (a, b, layer, acyclic, description) in predicates.items():
        add(entity('kps:' + name, 'relation-type', name.replace('-', ' '), source_kinds=a, target_kinds=b,
                   layer=layer, acyclic=acyclic, description=description))
    add(entity('english:legacy-route', 'sequence', 'Legacy Stage 0 through 7 route',
               positions={str(k): v for k, v in enumerate(['Foundations', 'Morphology and Lexicon', 'Syntax', 'Semantics', 'Pragmatics', 'Discourse and Information Structure', 'Phonetics and Phonology', 'Interfaces and Integration'])},
               ordering_meaning='An inherited introductory navigation route. Positions are neither empirical mastery claims nor mandatory processing or learning dependencies.'))


def make_claim(record, body):
    claim_id = record['id'] + ':claim:key-takeaway'
    claim = entity(claim_id, 'claim', record['label'] + ' — summary claim', owner=record['id'],
                   owner_version=record['version'], statement=section(Document(Path(record['content']), record, body), 'Key takeaway'),
                   scope='Only the qualified summary in the named owner; its assumptions, variety limits, examples and nonclaims remain in the full content.',
                   evidence_status='provisional', reviewed=None, extraction='key-takeaway-only',
                   granularity='summary-not-assumed-atomic')
    claim['domains'] = list(record['domains'])
    record['claims'] = [claim_id]
    record['claim_extraction'] = 'summary-only; all other body assertions require claim-by-claim review'
    return claim


def render_new_interface(item):
    source = item['source'].replace('-', ' ')
    target = item['target'].replace('-', ' ')
    related = '\n'.join(f'- [{name.replace("-", " ")}]({name}.md)' for name in item['uses'])
    return f'''# {item['label']}

## Key takeaway
{item['statement']}

## Summary
{item['statement']} This KPS 12 bridge is an authored provisional synthesis with a constructed illustration, not newly inspected empirical evidence.

## Purpose
Keep the two representations and their evidence requirements distinct while making their proposed correspondence inspectable.

## Representation
| Endpoint | Schematic fields |
|---|---|
| {source} | {', '.join(item['source_fields'])} |
| {target} | {', '.join(item['target_fields'])} |

The mapping uses `{item['predicate']}`. Field names identify an analytical record structure, not measured values or a complete formal linguistic theory.

## Worked interpretation
{item['example']}

## Assumptions and limits
{item['limitation']}

## Evaluation and counterevidence
Name the intended analysis, variety and relevant context. Inspect competing analyses and distinguish a prediction from an observation. A structural test of these records does not test the empirical correctness of the mapping. Missing observations remain missing.

## Evidence status
**Provisional.** No new external source inspection, independent expert review, audio measurement or learner outcome is claimed. This bridge is an authored synthesis of the existing distinctions below. Claim-level external support is pending.

## Related knowledge
{related}
'''


def port_tests(source, target):
    # Preserve the constructed-model tests, changing only their package wiring.
    tree = ast.parse((source / 'tests/test_domain.py').read_text(encoding='utf-8'))
    old_class = next(n for n in tree.body if isinstance(n, ast.ClassDef))
    names = {'test_plural_regular_patterns','test_past_regular_patterns','test_unknown_spelling_is_not_a_sound',
             'test_distinct_books_need_not_be_shared','test_shared_book_satisfies_both_readings','test_empty_quantifier_domains',
             'test_not_every_does_not_require_some_pass','test_five_finite_clauses','test_relative_ends_before_recipient_pp',
             'test_spans_are_nested_or_disjoint','test_recipient_is_not_patient','test_focus_is_answer_not_wh_word'}
    methods = [ast.unparse(n) for n in old_class.body if isinstance(n, ast.FunctionDef) and n.name in names]
    header = '"""Ported constructed-model regressions; not empirical validation."""\nimport json\nimport pathlib\nimport unittest\nfrom tools import linguistic_examples as examples\nROOT = pathlib.Path(__file__).resolve().parents[1]\n\nclass ConstructedModelTests(unittest.TestCase):\n'
    (target / 'tests/test_linguistic_fixtures.py').write_text(header + '\n\n'.join('\n'.join('    ' + line for line in text.splitlines()) for text in methods) + '\n', encoding='utf-8')
    # Port all 10 pronunciation Practice tests, retaining the substantive checks.
    text = (source / 'tests/test_pronunciation_practices.py').read_text(encoding='utf-8')
    text = text.replace("ROOT / 'practices/", "ROOT / 'knowledge/").replace("ROOT / 'references'", "ROOT / 'sources'")
    text = text.replace("self.assertEqual(doc.meta['type'], 'practice')", "self.assertEqual(doc.meta['roles'], ['kps:role:practice'])")
    text = text.replace("doc.meta['stages']", "doc.meta['sequences'][0]['positions']")
    text = text.replace("word.meta['composes']", "kps.targets(word, 'kps:composes')")
    text = text.replace("phone.meta.get('composes', [])", "kps.targets(phone, 'kps:composes')")
    text = text.replace("phone.meta.get('uses_practices', [])", "kps.targets(phone, 'kps:uses')")
    text = text.replace("'english:method:analyze-sound-realization', doc.meta['uses_methods']", "'english:analyze-sound-realization', kps.targets(doc, 'kps:uses')")
    text = text.replace("'english:model:phonological-word-model', doc.meta['uses_models']", "'english:phonological-word-model', kps.targets(doc, 'kps:uses')")
    (target / 'tests/test_pronunciation_practices.py').write_text(text, encoding='utf-8')


def migrate(source: Path, target: Path, assets: Path | None = None):
    source, target = source.resolve(), target.resolve()
    assets = assets or Path(__file__).resolve().parents[1]
    plan = json.loads((assets / 'migration/kps12-plan.json').read_text(encoding='utf-8'))
    if source == target or target.is_relative_to(source) or source.is_relative_to(target):
        raise ValueError('source and target must be separate non-nested directories')
    if target.exists() and any(target.iterdir()):
        raise ValueError('refusing to overwrite nonempty target: ' + str(target))
    if plan['base_commit'] != BASE:
        raise ValueError('unexpected migration baseline')
    baseline = {}
    for name, sha in plan['baseline_files'].items():
        data = (source / name).read_bytes()
        if digest(data) != sha:
            raise ValueError('pinned source changed: ' + name)
        baseline[name] = data
    target.mkdir(parents=True, exist_ok=True)
    # A frozen snapshot is not an active alternate ontology.
    for name, data in baseline.items():
        p = target / 'legacy/kps9' / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    templates = json.loads((assets / 'migration/template-manifest.json').read_text(encoding='utf-8'))
    for name in templates['files']:
        p = target / name
        p.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(assets / name, p)
    for name in ['LICENSE', '.gitignore', 'tools/linguistic_examples.py', 'data/integrated-example.json']:
        p = target / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(baseline[name])
    records = {}
    add_ontology(records, plan)
    old_docs = {}
    for name, data in baseline.items():
        if name.endswith('.md'):
            meta, body = legacy_parts(data.decode('utf-8'))
            if meta.get('type') in ROLE_NAMES + ['reference']:
                old_docs[name] = (meta, body)
    if len(old_docs) != 120:
        raise ValueError('expected 110 knowledge objects and 10 source records')
    ids = {m['id']: 'english:' + Path(name).stem for name, (m, _) in old_docs.items()}
    if len(set(ids.values())) != len(ids):
        raise ValueError('canonical identity collision')
    paths = {name: ('sources/' if m['type'] == 'reference' else 'knowledge/') + Path(name).name for name, (m, _) in old_docs.items()}
    paths['references/README.md'] = 'SOURCES.md'
    manifest = {'format': 12, 'baseline_commit': BASE, 'baseline_files': plan['baseline_files'],
                'identity_map': ids, 'path_map': paths, 'migrated': [],
                'scientific_review_performed': False, 'claim_extraction': 'key-takeaway-only'}
    excluded = {'id','type','version','language','stages','perspectives','references',*LEGACY_RELATIONS}
    for old_name, (meta, old_body) in sorted(old_docs.items()):
        ident = ids[meta['id']]
        old_doc = Document(Path(old_name), meta, old_body)
        label = next(h for n,h in old_doc.headings if n==1)
        record = entity(ident, 'source' if meta['type'] == 'reference' else 'knowledge', label)
        record.update({k:v for k,v in meta.items() if k not in excluded})
        record.update(version='0.2.0', aliases=[meta['id']], content=paths[old_name],
                      migration={'old_path': old_name, 'old_id': meta['id'], 'old_version': meta['version'],
                                 'legacy_metadata': meta, 'base_commit': BASE})
        body = rewrite_body(baseline[old_name].decode('utf-8'), old_name, paths)
        p = target / record['content']; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(body, encoding='utf-8')
        if record['kind'] == 'knowledge':
            record['roles'] = ['kps:role:' + meta['type']]
            record['domains'] = plan['classification'][old_name]
            record['sequences'] = [{'scheme':'english:legacy-route', 'positions': meta['stages']}]
            records[ident + ':claim:key-takeaway'] = make_claim(record, body)
        relations = []
        for key, role in LEGACY_RELATIONS.items():
            for old_target in meta.get(key, []):
                rel = {'predicate': 'kps:cites' if key == 'references' else 'kps:composes' if key == 'composes' else 'kps:related-to' if key == 'related_knowledge' else 'kps:uses',
                       'target': ids[old_target], 'legacy_predicate': key}
                if role in ROLE_NAMES:
                    rel['expected_target_role'] = 'kps:role:' + role
                relations.append(rel)
                if key == 'references':
                    evidence = entity('english:evidence:' + digest(ident + '\0' + ids[old_target])[:24], 'evidence',
                                      label + ' — legacy source context', about=ident, source=ids[old_target],
                                      assessment_relation='context-only',
                                      assessment='Preserves an existing document citation. No claim-level support is inferred by migration.',
                                      inspection_extent='Historical source-record inspection extent is retained; migration performs no new source inspection.',
                                      locator=None, record_origin='legacy-citation-migration')
                    records[evidence['id']] = evidence
        record['relations'] = relations
        records[ident] = record
        old_path = target / old_name; old_path.parent.mkdir(parents=True, exist_ok=True)
        old_path.write_text(redirect(baseline[old_name].decode('utf-8'), old_name, paths[old_name]), encoding='utf-8')
        manifest['migrated'].append({'old_path': old_name, 'id': ident, 'content': record['content'],
                                     'initial_version': record['version'], 'canonical_body_sha256': digest(body),
                                     'transform': 'frontmatter-to-json-and-relative-link-rewrite-v1',
                                     'maintenance_note_added': old_name == 'practices/maintain-english-package.md'})
    # Migrate five existing mappings and add five explicitly unverified bridges.
    for item in plan['interfaces'] + plan['new_interfaces']:
        ident = 'english:' + item['slug']
        domains = ['linguistics:' + item['source_domain'], 'linguistics:' + item['target_domain']]
        for side in ('source', 'target'):
            repid = 'english:representation:' + item[side]
            rep = entity(repid, 'representation', item[side].replace('-', ' ').capitalize(),
                         structure={'record_fields': item[side + '_fields'], 'observation_status': 'schematic; no token measurements'},
                         scope='An analytical representation for the documented interface, not a universal ontology or observed token.',
                         evidence_status='provisional', reviewed=None)
            rep['domains'] = ['linguistics:' + item[side + '_domain']]
            if repid in records and (records[repid]['structure'] != rep['structure'] or records[repid]['domains'] != rep['domains']):
                raise ValueError('inconsistent shared representation: ' + repid)
            records[repid] = rep
        if ident not in records:
            body = render_new_interface(item)
            r = entity(ident, 'interface', item['label'], content='knowledge/' + item['slug'] + '.md',
                       evidence_status='provisional', reviewed=None,
                       source_status='external-support-pending', basis_kind='KPS 12 authored bridge synthesis; constructed illustration; independent review pending')
            r['version'] = '0.2.0'; r['roles'] = ['kps:role:model']; r['domains'] = domains
            r['sequences'] = [{'scheme': 'english:legacy-route', 'positions': [7]}]
            r['relations'] = [{'predicate': 'kps:uses', 'target':'english:' + name} for name in item['uses']]
            records[ident] = r
            records[ident + ':claim:key-takeaway'] = make_claim(r, body)
            (target / r['content']).write_text(body, encoding='utf-8')
        r = records[ident]
        r['kind'] = 'interface'
        r['domains'] = sorted(set(r['domains']) | set(domains))
        records[r['claims'][0]]['domains'] = list(r['domains'])
        r['mapping'] = {'source':'english:representation:' + item['source'], 'target':'english:representation:' + item['target'],
                        'predicate':item['predicate'], 'claim':r['claims'][0], 'scope':'The working analysis, context and variety limits in ' + r['content'] + '; not a neural processing claim.',
                        'cardinality':'unspecified'}
    for r in records.values():
        write_record(target, r)
    for name in ['SCOPE.md', 'PRONUNCIATION.md']:
        text = rewrite_body(baseline[name].decode('utf-8'), name, paths)
        (target/name).write_text(text,encoding='utf-8')
    notice = rewrite_body(baseline['NOTICE.md'].decode('utf-8'), 'NOTICE.md', paths)
    notice = notice.replace('AUTHORING.md, validate.py and test_validate.py are copied unchanged',
                            'The historical legacy/kps9/AUTHORING.md, legacy/kps9/validate.py and legacy/kps9/test_validate.py are copied unchanged')
    notice = notice.replace('Upstream hashes are recorded in upstream-lock.json.', 'Historical upstream hashes are recorded in legacy/kps9/upstream-lock.json. Active KPS 12 tooling is newly authored and does not claim to be unchanged upstream tooling.')
    (target/'NOTICE.md').write_text(notice, encoding='utf-8')
    changelog = rewrite_body(baseline['CHANGELOG.md'].decode('utf-8'), 'CHANGELOG.md', paths)
    change = '\n## Version 0 2 0 KPS 12\n\nFull entity-centric migration to the local 12.0.0-draft.1 profile. Preserves 110 knowledge objects and 10 sources; introduces explicit domains, versioned summary claims, context-only evidence, typed mappings and five provisional bridge Models. No independent scientific review or upstream KPS release is claimed.\n'
    changelog = changelog.replace('\n## Integrated pronunciation Practices', change + '\n## Integrated pronunciation Practices', 1)
    (target/'CHANGELOG.md').write_text(changelog,encoding='utf-8')
    (target/'REVIEW.md').write_text('# Review policy\n\n## Key takeaway\nEditorial review, source inspection and independent scientific review are different records.\n\n## Summary\nEvery linguistic knowledge entity and extracted summary claim remains provisional. The review queue exposes body claims not yet extracted and the distinction between context-only source links and claim-level support.\n\n## Promotion\nA version-specific review must name an actual reviewer, inspected claims, passages, limitations and findings. No automated tool establishes that a review occurred. See [AUTHORING](AUTHORING.md), [CHECKS](CHECKS.md) and [the review queue](REVIEW-QUEUE.md).\n',encoding='utf-8')
    (target/'references/README.md').write_text('# Source register compatibility redirect\n\n## Key takeaway\nThe active KPS 12 source register has moved.\n\n## Summary\nRead the [source register](../SOURCES.md). Publication records retain their historical access limitations.\n',encoding='utf-8')
    pub = {'package':'English Linguistics KPS', 'version':'0.2.0', 'kps_language':'12.x', 'profile_version':PROFILE,
           'profile_status':'experimental local implementation', 'scientific_status':'provisional', 'independent_review':False,
           'created':'2026-10-13', 'entity_schema':'kps:12:entity', 'graph_format':12,
           'baseline_commit':BASE, 'license':'MIT', 'scope':'Ten-domain English knowledge architecture; broad provisional content, not exhaustive or scientifically certified.'}
    (target/'publication.json').write_text(dump(pub),encoding='utf-8')
    (target/'upstream-lock.json').write_text(dump({'scope':'historical KPS 9 attribution only', 'active_profile':PROFILE,
                                               'legacy_lock':'legacy/kps9/upstream-lock.json', 'upstream_kps12_release_claimed':False}),encoding='utf-8')
    (target/'migration/manifest.json').write_text(dump(manifest),encoding='utf-8')
    # This is a structural migration baseline, never a scientific-review promotion.
    (target/'summary-dependencies.json').write_text(dump(current_dependencies(target, records)),encoding='utf-8')
    port_tests(source,target)
    for name,text in generated(target,records,{i:record_filename(i) for i in records}).items():
        p=target/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
    result=validate(target)
    if not result['ok']:
        raise ValueError('generated migration failed validation:\n' + dump(result))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--target',type=Path,required=True)
    args=parser.parse_args()
    try:
        print(dump(migrate(args.source,args.target)))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        parser.exit(1,str(exc)+'\n')
