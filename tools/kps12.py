#!/usr/bin/env python3
"""KPS 12 entity profile: validation, deterministic views and read-only queries.

Standard library only. Structural checks do not establish scientific truth.
The profile is local to this package; it is not an upstream KPS release claim.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from dataclasses import dataclass
from urllib.parse import unquote, urlsplit

PROFILE = '12.0.0-draft.1'
LANGUAGE = 'KPS 12.x'
KINDS = {'knowledge', 'source', 'domain', 'role', 'relation-type',
         'representation', 'interface', 'claim', 'evidence', 'sequence'}
KNOWLEDGE = {'knowledge', 'interface'}
ID_PATTERN = re.compile(r'^[a-z][a-z0-9-]*(?::[a-z0-9][a-z0-9-]*)+$')
VERSION_PATTERN = re.compile(r'^\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?$')
ROLES = ('concept', 'principle', 'model', 'method', 'practice')


def pairs_unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: ' + key)
        result[key] = value
    return result


def read_json(path: Path):
    def reject_constant(value):
        raise ValueError('non-finite JSON number: ' + value)
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs_unique, parse_constant=reject_constant)


def dump(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + '\n'


def digest(value: str | bytes) -> str:
    return hashlib.sha256(value.encode('utf-8') if isinstance(value, str) else value).hexdigest()


def safe_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError('expected a nonempty relative path')
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError('path leaves package: ' + relative)
    return result


def slug(text: str) -> str:
    return re.sub(r' +', '-', re.sub(r'[^\w\- ]', '', text.strip().lower()))


def live_markdown(text: str) -> str:
    return re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*(?:\n|$)', '', text)


def meaningful(text: str) -> str:
    return re.sub(r'[^\w\s]', ' ', re.sub(r'\[[^\]]*\]\([^)]*\)', '', text))


@dataclass
class Document:
    path: Path
    meta: dict
    body: str

    @property
    def live(self):
        return live_markdown(self.body)

    @property
    def headings(self):
        return [(len(m[0]), m[1].strip()) for m in re.findall(r'(?m)^(#{1,6})[ \t]+(.+)$', self.live)]

    @property
    def links(self):
        return re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', self.live)


def section(doc: Document, heading: str) -> str:
    match = re.search(r'(?m)^## (?:' + heading + r')\s*$', doc.body)
    if not match:
        return ''
    tail = doc.body[match.end():]
    return re.split(r'(?m)^## ', tail, maxsplit=1)[0].strip()


def find_root(path: Path) -> Path:
    for parent in (path.parent, *path.parents):
        if (parent / 'publication.json').is_file() and (parent / 'entities').is_dir():
            return parent
    raise ValueError('no KPS 12 package root for ' + str(path))


def load(root: Path) -> tuple[dict, dict]:
    records, paths = {}, {}
    for path in sorted((root / 'entities').glob('*.json')):
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('entity record leaves package: ' + str(path))
        record = read_json(path)
        if not isinstance(record, dict) or not isinstance(record.get('id'), str):
            raise ValueError(str(path) + ': entity object with string id required')
        if record['id'] in records:
            raise ValueError('duplicate entity id: ' + record['id'])
        records[record['id']] = record
        paths[record['id']] = path.relative_to(root).as_posix()
    if not records:
        raise ValueError('empty entity store')
    return records, paths


def parse(path: Path) -> Document:
    """Read neutral Markdown and resolve its metadata from the entity store."""
    path = Path(path).resolve()
    root = find_root(path)
    records, _ = load(root)
    matches = [r for r in records.values() if r.get('content') == path.relative_to(root).as_posix()]
    if len(matches) != 1:
        raise ValueError('content must have exactly one canonical owner: ' + str(path))
    return Document(path, matches[0], path.read_text(encoding='utf-8'))


def targets(record: dict | Document, predicate: str) -> list[str]:
    if isinstance(record, Document):
        record = record.meta
    return [r['target'] for r in record.get('relations', []) if r['predicate'] == predicate]


def make_edge(source: str, predicate: str, target: str, layer: str, **extra) -> dict:
    key = '\0'.join((source, predicate, target, str(extra.get('owner', ''))))
    return {'id': 'kps:edge:' + digest(key)[:24], 'source': source,
            'predicate': predicate, 'target': target, 'layer': layer, **extra}


def graph(records: dict, paths: dict) -> dict:
    edges = []
    for ident, r in sorted(records.items()):
        for role in r.get('roles', []):
            edges.append(make_edge(ident, 'kps:classified-as-role', role, 'classification'))
        for domain in r.get('domains', []):
            edges.append(make_edge(ident, 'kps:in-domain', domain, 'classification'))
        for parent in r.get('parents', []):
            edges.append(make_edge(ident, 'kps:broader-domain', parent, 'classification'))
        for rel in r.get('relations', []):
            definition = records.get(rel.get('predicate'), {})
            edges.append(make_edge(ident, rel['predicate'], rel['target'],
                                   definition.get('layer', 'invalid'),
                                   **{k: v for k, v in rel.items() if k not in {'predicate', 'target'}}))
        for claim in r.get('claims', []):
            edges.append(make_edge(ident, 'kps:asserts', claim, 'claim'))
        for seq in r.get('sequences', []):
            edges.append(make_edge(ident, 'kps:in-sequence', seq['scheme'], 'navigation', positions=seq['positions']))
        if r['kind'] == 'interface':
            m = r['mapping']
            edges.extend([
                make_edge(ident, 'kps:source-representation', m['source'], 'interface'),
                make_edge(ident, 'kps:target-representation', m['target'], 'interface'),
                make_edge(m['source'], m['predicate'], m['target'], 'semantic',
                          owner=ident, claim=m['claim'], scope=m['scope'], cardinality=m['cardinality'],
                          evidence_status=r['evidence_status'])])
        if r['kind'] == 'evidence':
            edges.append(make_edge(ident, 'kps:evidence-from', r['source'], 'evidence'))
            edges.append(make_edge(ident, 'kps:evidence-about', r['about'], 'evidence',
                                   assessment=r['assessment_relation'], locator=r.get('locator')))
    return {'format': 12, 'profile': PROFILE,
            'description': 'Explicit entities and qualified edges; no causal, truth or transitive inference.',
            'nodes': [dict(records[i], record_path=paths[i]) for i in sorted(records)],
            'edges': sorted(edges, key=lambda e: (e['source'], e['predicate'], e['target'], e['id']))}


def cycle_nodes(adjacency: dict) -> list[str]:
    visiting, complete, cycles = set(), set(), set()
    def walk(node):
        if node in visiting:
            cycles.add(node)
            return
        if node in complete:
            return
        visiting.add(node)
        for target in adjacency.get(node, []):
            walk(target)
        visiting.remove(node)
        complete.add(node)
    for ident in adjacency:
        walk(ident)
    return sorted(cycles)


def current_dependencies(root: Path, records: dict) -> dict:
    hashes = {}
    for ident, r in sorted(records.items()):
        if r.get('content'):
            hashes[ident] = digest(safe_path(root, r['content']).read_bytes())
    dependencies = {i: sorted(set(rel['target'] for rel in r.get('relations', [])
                                  if rel['predicate'] in {'kps:uses', 'kps:cites', 'kps:composes'}))
                    for i, r in sorted(records.items()) if r['kind'] in KNOWLEDGE}
    return {'format': 12, 'content_sha256': hashes, 'dependencies': dependencies}


def schema_errors(value, schema, path='$') -> list[str]:
    """Validate the deliberately bounded JSON Schema vocabulary used by this profile.

    No external references, network resolution, custom formats or inference.
    The shipped schema only uses the supported keywords below.
    """
    errors = []
    types = {'object': lambda v: isinstance(v, dict),
             'array': lambda v: isinstance(v, list),
             'string': lambda v: isinstance(v, str),
             'integer': lambda v: type(v) is int,
             'number': lambda v: type(v) in (int, float),
             'boolean': lambda v: type(v) is bool,
             'null': lambda v: v is None}
    expected = schema.get('type')
    if expected:
        expected = [expected] if isinstance(expected, str) else expected
        if not any(types[t](value) for t in expected):
            return [path + ': wrong JSON type']
    if 'const' in schema and value != schema['const']:
        errors.append(path + ': wrong constant')
    if 'enum' in schema and value not in schema['enum']:
        errors.append(path + ': value is outside enum')
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0):
            errors.append(path + ': empty string')
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            errors.append(path + ': invalid string pattern')
    if isinstance(value, dict):
        for key in schema.get('required', []):
            if key not in value:
                errors.append(path + ': missing ' + key)
        if len(value) < schema.get('minProperties', 0):
            errors.append(path + ': not enough properties')
        props = schema.get('properties', {})
        for key, child in value.items():
            if key in props:
                errors.extend(schema_errors(child, props[key], path + '.' + key))
            elif schema.get('additionalProperties') is False:
                errors.append(path + ': unknown property ' + key)
            elif isinstance(schema.get('additionalProperties'), dict):
                errors.extend(schema_errors(child, schema['additionalProperties'], path + '.' + key))
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errors.append(path + ': not enough array items')
        if schema.get('uniqueItems') and len(value) != len({dump(v) for v in value}):
            errors.append(path + ': duplicate array item')
        if 'items' in schema:
            for n, child in enumerate(value):
                errors.extend(schema_errors(child, schema['items'], path + '[' + str(n) + ']'))
    for child in schema.get('allOf', []):
        errors.extend(schema_errors(value, child, path))
    if 'if' in schema and not schema_errors(value, schema['if'], path):
        errors.extend(schema_errors(value, schema.get('then', {}), path))
    return errors


def validate(root: Path, check_views: bool = True, check_dependencies: bool = True) -> dict:
    root = Path(root).resolve()
    errors = []
    def fail(code, ident, message):
        errors.append({'code': code, 'entity': ident, 'message': message})
    try:
        pub = read_json(root / 'publication.json')
        records, paths = load(root)
        if pub.get('kps_language') != '12.x' or pub.get('profile_version') != PROFILE:
            fail('profile', 'publication', 'expected local KPS 12 draft profile')
        if pub.get('independent_review') is not False:
            fail('review', 'publication', 'migration does not confer independent review')
    except (OSError, ValueError, TypeError) as exc:
        return {'ok': False, 'errors': [{'code': 'load', 'entity': '', 'message': str(exc)}], 'stats': {}}

    try:
        schema = read_json(root / 'schema/entity.schema.json')
        for ident, r in records.items():
            for message in schema_errors(r, schema):
                fail('serialization', ident, message)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        fail('serialization', 'schema', str(exc))
    if errors:
        return {'ok': False, 'profile': PROFILE, 'errors': errors, 'stats': {}}

    aliases, contents = {}, {}
    required_by_kind = {
        'knowledge': ['content', 'claims', 'claim_extraction', 'evidence_status'],
        'interface': ['content', 'claims', 'claim_extraction', 'evidence_status', 'mapping'],
        'source': ['content', 'creator', 'publication', 'publication_date', 'date_basis', 'accessed', 'access_extent'],
        'domain': ['parents', 'scope', 'top_level'],
        'role': ['description', 'required_sections'],
        'relation-type': ['source_kinds', 'target_kinds', 'layer', 'acyclic', 'description'],
        'representation': ['structure', 'scope'],
        'claim': ['owner', 'owner_version', 'statement', 'scope', 'evidence_status', 'extraction'],
        'evidence': ['about', 'source', 'assessment_relation', 'assessment', 'inspection_extent', 'locator'],
        'sequence': ['positions', 'ordering_meaning']}

    def ref(ident, target, kinds=None):
        found = records.get(target) if isinstance(target, str) else None
        if found is None:
            fail('unresolved', ident, 'unknown canonical target: ' + str(target))
            return None
        if kinds and found['kind'] not in kinds:
            fail('endpoint-kind', ident, str(target) + ' must be one of ' + str(sorted(kinds)))
        return found

    for ident, r in records.items():
        kind = r.get('kind')
        if not ID_PATTERN.fullmatch(ident):
            fail('identity', ident, 'invalid namespaced identity')
        for field in ['schema', 'kind', 'label', 'version', 'roles', 'domains', 'status', 'aliases', 'relations']:
            if field not in r:
                fail('required', ident, 'missing ' + field)
        if r.get('schema') != 'kps:12:entity' or kind not in KINDS:
            fail('schema', ident, 'invalid schema or structural kind')
            continue
        if not isinstance(r.get('label'), str) or not r['label'].strip():
            fail('label', ident, 'nonempty label required')
        if not VERSION_PATTERN.fullmatch(str(r.get('version', ''))):
            fail('version', ident, 'invalid entity version')
        if r.get('status') not in {'draft', 'active', 'deprecated'}:
            fail('status', ident, 'unsupported lifecycle state')
        for field in required_by_kind[kind]:
            if field not in r:
                fail('required', ident, 'missing ' + field)
        arrays_ok = True
        for field in ['roles', 'domains', 'aliases', 'relations', 'claims', 'sequences']:
            if not isinstance(r.get(field, []), list):
                fail('array', ident, field + ' must be an array')
                arrays_ok = False
        if not arrays_ok:
            continue
        for field in ['roles', 'domains', 'aliases', 'claims']:
            values = r.get(field, [])
            if any(not isinstance(v, str) for v in values) or len(values) != len(set(map(str, values))):
                fail('unique-list', ident, field + ' must contain unique strings')
        for alias in r.get('aliases', []):
            if alias in aliases or alias in records:
                fail('alias', ident, 'ambiguous or shadowing alias: ' + str(alias))
            aliases[str(alias)] = ident
        for role in r.get('roles', []):
            ref(ident, role, {'role'})
        for domain in r.get('domains', []):
            ref(ident, domain, {'domain'})
        if kind in KNOWLEDGE and (not r.get('roles') or not r.get('domains') or not r.get('claims')):
            fail('knowledge-facets', ident, 'knowledge needs roles, domains and explicit claims')
        if kind not in KNOWLEDGE and r.get('roles'):
            fail('role-kind', ident, 'this draft profile assigns the five roles to knowledge/interface records only')
        if kind in KNOWLEDGE | {'claim', 'representation'}:
            if r.get('evidence_status') not in {'provisional', 'reviewed'}:
                fail('evidence-status', ident, 'explicit evidence status required')
            if r.get('evidence_status') == 'provisional' and r.get('reviewed') is not None:
                fail('review', ident, 'provisional entity cannot claim a reviewed date')
            if r.get('evidence_status') == 'reviewed':
                review_paths = r.get('review_records', [])
                if not review_paths:
                    fail('review', ident, 'reviewed status requires version-specific review records')
                for review_path in review_paths:
                    try:
                        review = read_json(safe_path(root, review_path))
                        if review.get('entity') != ident or review.get('version') != r['version'] or not review.get('reviewer') or not review.get('findings'):
                            fail('review', ident, 'incomplete or mismatched review record')
                    except (OSError, ValueError, TypeError):
                        fail('review', ident, 'unreadable review record')
        if r.get('content'):
            try:
                p = safe_path(root, r['content'])
                if r['content'] in contents:
                    fail('content-owner', ident, 'canonical content has multiple owners')
                contents[r['content']] = ident
                body = p.read_text(encoding='utf-8')
                doc = Document(p, r, body)
                if body.startswith('---\n'):
                    fail('old-frontmatter', ident, 'canonical metadata belongs in JSON, not legacy role frontmatter')
                if sum(n == 1 for n, _ in doc.headings) != 1:
                    fail('heading', ident, 'exactly one top-level title required')
                for heading in ('Key takeaway', 'Summary'):
                    if not section(doc, heading):
                        fail('self-contained', ident, 'missing ' + heading)
                for role in r.get('roles', []):
                    for required in records.get(role, {}).get('required_sections', []):
                        if not section(doc, required):
                            fail('role-contract', ident, 'missing role section: ' + required)
                if kind in KNOWLEDGE and r.get('evidence_status') == 'provisional':
                    if 'provisional' not in section(doc, 'Evidence status').lower():
                        fail('visible-status', ident, 'provisional status absent from content')
                if 'kps:role:practice' in r.get('roles', []):
                    stages = [h for n, h in doc.headings if n == 2 and re.match(r'Stage\d+ ', h)]
                    if not stages or [int(re.match(r'Stage(\d+)', h)[1]) for h in stages] != list(range(1, len(stages) + 1)):
                        fail('practice-stage', ident, 'local stages must be consecutively numbered')
                    if stages != r.get('stage_titles'):
                        fail('practice-stage', ident, 'stage_titles mismatch')
                    for h in stages:
                        text = section(doc, re.escape(h))
                        if '#' + slug(h) not in doc.links:
                            fail('practice-stage-map', ident, 'missing stage map link')
                        for label in ('Goal', 'Why', 'What to do', 'What to observe', 'Success signal', 'Next'):
                            if not re.search(r'\*\*' + label + r':\*\*\s+\S', text):
                                fail('practice-local', ident, 'stage lacks ' + label)
                if kind == 'source':
                    if not section(doc, 'Nonclaims') or not any(urlsplit(x).scheme == 'https' for x in doc.links):
                        fail('source-boundary', ident, 'source needs external locator and nonclaims')
            except (OSError, ValueError, TypeError) as exc:
                fail('content', ident, str(exc))
        seen_relations = set()
        for rel in r.get('relations', []):
            if not isinstance(rel, dict) or not isinstance(rel.get('predicate'), str) or not isinstance(rel.get('target'), str):
                fail('relation', ident, 'predicate and canonical target required')
                continue
            key = (rel['predicate'], rel['target'])
            if key in seen_relations:
                fail('relation', ident, 'duplicate relation')
            seen_relations.add(key)
            pred = ref(ident, rel['predicate'], {'relation-type'})
            target = ref(ident, rel['target'])
            if pred and target:
                if kind not in pred.get('source_kinds', []) or target['kind'] not in pred.get('target_kinds', []):
                    fail('relation-endpoint', ident, 'invalid endpoints for ' + rel['predicate'])
                if pred.get('layer') == 'semantic' and not ref(ident, rel.get('claim'), {'claim'}):
                    fail('semantic-claim', ident, 'semantic relationship requires an explicit claim')
                if rel.get('expected_target_role') and rel['expected_target_role'] not in target.get('roles', []):
                    fail('target-role', ident, 'migrated target role restriction not met')
                if rel['predicate'] == 'kps:composes' and ('kps:role:practice' not in r['roles'] or 'kps:role:practice' not in target['roles']):
                    fail('composition', ident, 'composes requires Practice roles at both ends')
        for sequence in r.get('sequences', []):
            if not isinstance(sequence, dict):
                fail('sequence', ident, 'sequence membership must be an object')
                continue
            seq = ref(ident, sequence.get('scheme'), {'sequence'})
            positions = sequence.get('positions')
            if not isinstance(positions, list) or not positions or any(type(v) is not int for v in positions):
                fail('sequence', ident, 'positions must be nonempty integer array')
            elif seq and any(str(v) not in seq.get('positions', {}) for v in positions):
                fail('sequence', ident, 'unknown position')
        for cid in r.get('claims', []):
            c = ref(ident, cid, {'claim'})
            if c and c.get('owner') != ident:
                fail('claim-owner', ident, 'listed claim belongs to another entity')
        if kind == 'domain':
            parents = r.get('parents', [])
            if not isinstance(parents, list):
                fail('domain', ident, 'parents must be a list')
            else:
                for parent in parents:
                    ref(ident, parent, {'domain'})
            if not isinstance(r.get('scope'), str) or not r['scope'].strip():
                fail('domain-scope', ident, 'domain needs defined scope')
        elif kind == 'relation-type':
            for field in ('source_kinds', 'target_kinds'):
                if not isinstance(r.get(field), list) or not r[field] or not set(r[field]) <= KINDS:
                    fail('predicate-signature', ident, 'invalid ' + field)
            if type(r.get('acyclic')) is not bool:
                fail('predicate-signature', ident, 'acyclic must be explicit boolean')
        elif kind == 'claim':
            owner = ref(ident, r.get('owner'), KNOWLEDGE)
            if owner:
                if ident not in owner.get('claims', []):
                    fail('claim-owner', ident, 'owner does not declare this claim')
                if r.get('owner_version') != owner['version']:
                    fail('claim-version', ident, 'claim is not scoped to the current owner version')
                if r.get('extraction') == 'key-takeaway-only' and owner.get('content'):
                    try:
                        doc = Document(root / owner['content'], owner, (root / owner['content']).read_text(encoding='utf-8'))
                        if r.get('statement') != section(doc, 'Key takeaway'):
                            fail('claim-drift', ident, 'extracted claim differs from its source section')
                    except OSError:
                        pass
            if not isinstance(r.get('statement'), str) or not r['statement'].strip() or not r.get('scope'):
                fail('claim', ident, 'statement and scope required')
        elif kind == 'representation':
            if not r.get('domains') or not isinstance(r.get('structure'), dict) or not r['structure']:
                fail('representation', ident, 'schematic structure and domain membership required')
        elif kind == 'interface':
            m = r.get('mapping')
            if not isinstance(m, dict):
                fail('interface', ident, 'mapping object required')
                continue
            a = ref(ident, m.get('source'), {'representation'})
            b = ref(ident, m.get('target'), {'representation'})
            c = ref(ident, m.get('claim'), {'claim'})
            p = ref(ident, m.get('predicate'), {'relation-type'})
            if a and b and not (set(a['domains']) | set(b['domains'])) <= set(r['domains']):
                fail('interface-domains', ident, 'interface must declare both endpoint domains')
            if c and c.get('owner') != ident:
                fail('interface-claim', ident, 'mapping claim must belong to this interface')
            if p and (p.get('layer') != 'semantic' or 'representation' not in p.get('source_kinds', []) or 'representation' not in p.get('target_kinds', [])):
                fail('interface-predicate', ident, 'mapping must use a semantic predicate permitting representation endpoints')
            if not m.get('scope') or m.get('cardinality') not in {'unspecified', 'one-to-one', 'one-to-many', 'many-to-one', 'many-to-many'}:
                fail('interface-scope', ident, 'scope and explicit cardinality required')
        elif kind == 'evidence':
            source = ref(ident, r.get('source'), {'source'})
            about = ref(ident, r.get('about'))
            relation = r.get('assessment_relation')
            if relation not in {'context-only', 'supports', 'qualifies', 'contradicts'}:
                fail('evidence-relation', ident, 'unsupported assessment relation')
            if relation != 'context-only':
                if about and about['kind'] != 'claim':
                    fail('evidence-target', ident, 'substantive evidence must target a specific claim')
                for field in ('locator', 'assessment', 'inspection_extent'):
                    if not isinstance(r.get(field), str) or not r[field].strip():
                        fail('evidence-locator', ident, 'claim-level evidence needs ' + field)
                if r.get('record_origin') == 'legacy-citation-migration':
                    fail('evidence-promotion', ident, 'legacy citations cannot automatically support a claim')
            if relation == 'context-only' and about and about['kind'] not in KNOWLEDGE:
                fail('context-evidence', ident, 'context-only citations attach to documents, not claims')

    domain_edges = {i: r.get('parents', []) for i, r in records.items()
                    if r['kind'] == 'domain' and isinstance(r.get('parents'), list)}
    for ident in cycle_nodes(domain_edges):
        fail('domain-cycle', ident, 'domain hierarchy is cyclic')
    for pred, definition in records.items():
        if definition['kind'] == 'relation-type' and definition.get('acyclic'):
            adjacency = {i: targets(r, pred) for i, r in records.items()}
            for ident in cycle_nodes(adjacency):
                fail('relation-cycle', ident, 'cycle in ' + pred)
    for folder in ('knowledge', 'sources'):
        for p in (root / folder).glob('*.md'):
            if p.relative_to(root).as_posix() not in contents:
                fail('orphan-content', str(p), 'Markdown content has no canonical entity')
    if not errors:
        check_links(root, errors)
    if check_dependencies:
        try:
            current = current_dependencies(root, records)
            saved = read_json(root / 'summary-dependencies.json')
            if current != saved:
                fail('dependency-review', 'summary-dependencies.json',
                     'content or dependencies changed; inspect affected summaries and submit an explicit editorial review record')
        except (OSError, ValueError, TypeError) as exc:
            fail('dependency-review', 'summary-dependencies.json', str(exc))
    # Generated views never repair invalid canonical data during validation.
    if check_views and not errors:
        for name, text in generated(root, records, paths).items():
            p = root / name
            if not p.is_file() or p.read_text(encoding='utf-8') != text:
                fail('stale-view', name, 'regenerate with tools/build_navigation.py')
    if not errors:
        g = graph(records, paths)
        if len({e['id'] for e in g['edges']}) != len(g['edges']):
            fail('edge-identity', 'graph', 'duplicate qualified edge identities')
    counts = collections.Counter(r['kind'] for r in records.values())
    stats = {'entities': len(records), 'knowledge_entities': sum(counts[k] for k in KNOWLEDGE),
             'sources': counts['source'], 'claims': counts['claim'], 'interfaces': counts['interface'],
             'top_level_linguistic_domains': sum(r['kind'] == 'domain' and r.get('top_level') is True for r in records.values()),
             'by_kind': dict(sorted(counts.items())),
             'substantive_evidence_records': sum(r['kind'] == 'evidence' and r.get('assessment_relation') != 'context-only' for r in records.values())}
    return {'ok': not errors, 'profile': PROFILE,
            'scope': 'Structure, declared relationships and provenance consistency; not linguistic certification.',
            'stats': stats, 'errors': errors}


def check_links(root: Path, errors: list):
    paths = list(root.glob('*.md'))
    for folder in ('knowledge', 'sources', 'views', 'spec', 'concepts', 'principles', 'models', 'methods', 'practices', 'references'):
        paths.extend((root / folder).rglob('*.md'))
    heading_cache = {}
    for p in sorted(set(paths)):
        doc = Document(p, {}, p.read_text(encoding='utf-8'))
        for link in doc.links:
            part = urlsplit(link)
            if part.scheme or part.netloc:
                continue
            try:
                target = (p.parent / unquote(part.path)).resolve() if part.path else p.resolve()
                if not target.is_relative_to(root.resolve()) or not target.is_file():
                    raise ValueError('unresolved or escaping local link: ' + link)
                if part.fragment and target.suffix == '.md':
                    if target not in heading_cache:
                        target_doc = Document(target, {}, target.read_text(encoding='utf-8'))
                        heading_cache[target] = {slug(h) for _, h in target_doc.headings}
                    if unquote(part.fragment) not in heading_cache[target]:
                        raise ValueError('unknown heading fragment: ' + link)
            except (OSError, ValueError) as exc:
                errors.append({'code': 'local-link', 'entity': p.relative_to(root).as_posix(), 'message': str(exc)})


def opening(title: str, takeaway: str) -> str:
    return f'# {title}\n\n## Key takeaway\n{takeaway}\n\n## Summary\nGenerated from canonical KPS 12 entities. Classification and structural coverage do not establish completeness or scientific review.\n'


def generated(root: Path, records: dict | None = None, paths: dict | None = None) -> dict:
    if records is None:
        records, paths = load(root)
    knowledge = sorted((r for r in records.values() if r['kind'] in KNOWLEDGE), key=lambda r: (r['label'].lower(), r['id']))
    domains = sorted((r for r in records.values() if r['kind'] == 'domain'), key=lambda r: r['label'])
    interfaces = [r for r in knowledge if r['kind'] == 'interface']
    def link(r, prefix=''):
        return f'[{r["label"]}]({prefix}{r.get("content", paths[r["id"]])})'
    def role_names(r):
        return ', '.join(records[i]['label'] for i in r.get('roles', []))
    out = {'knowledge-graph.json': dump(graph(records, paths))}
    index = opening('Knowledge by role', 'Roles classify entities; folders do not define their identity.')
    for role in ROLES:
        index += '\n## ' + role.capitalize() + '\n\n'
        for r in knowledge:
            if 'kps:role:' + role in r['roles']:
                index += f'- {link(r)} — {r["evidence_status"]}.\n'
    out['INDEX.md'] = index
    domain_index = opening('Linguistic domains', 'Ten independently browsable domains share one canonical entity store.')
    coverage = opening('Domain and sequence coverage', 'Unrepresented subdomains are explicit gaps, not silently inferred coverage.')
    rows = []
    for d in domains:
        direct = [r for r in knowledge if d['id'] in r['domains']]
        child_ids = {r['id'] for r in domains if d['id'] in r.get('parents', [])}
        children = [r for r in domains if r['id'] in child_ids]
        relevant = [r for r in knowledge if d['id'] in r['domains'] or child_ids.intersection(r['domains'])]
        if not d.get('top_level'):
            continue
        page = 'views/domains/' + d['id'].split(':')[-1] + '.md'
        domain_index += f'- [{d["label"]}]({page}) — {len(relevant)} knowledge entities, {len(children)} registered subdomains.\n'
        text = opening(d['label'], d['scope']) + '\n## Internal structure and gaps\n\n'
        text += '| Subdomain | Explicitly classified knowledge entities | Status |\n|---|---:|---|\n'
        for child in children:
            count = sum(child['id'] in r['domains'] for r in knowledge)
            text += f'| {child["label"]} | {count} | {"Represented; depth unreviewed" if count else "Unrepresented; content needed"} |\n'
        text += '\n## Canonical knowledge\n\n'
        for r in relevant:
            text += f'- {link(r, "../../")} — {role_names(r)}; {r["evidence_status"]}.\n'
        text += '\n## Interfaces\n\n'
        for r in interfaces:
            if d['id'] in r['domains']:
                text += '- ' + link(r, '../../') + ' — scoped, provisional mapping.\n'
        text += '\n## Evidence limits\n\nLegacy source links retain their original inspection limits. Claim extraction is summary-only; body assertions still require claim-by-claim review.\n'
        out[page] = text
        rows.append((d['label'], len(relevant), len(children), sum(not any(c['id'] in r['domains'] for r in knowledge) for c in children)))
    domain_index += '\n## Additional classification\n\nFoundations and knowledge-maintenance entities are also classified, without pretending to be an eleventh linguistic subsystem.\n'
    out['DOMAINS.md'] = domain_index
    coverage += '\n## Ten-domain coverage\n\n| Domain | Entities | Subdomains | Unrepresented subdomains |\n|---|---:|---:|---:|\n'
    for row in rows:
        coverage += '| ' + ' | '.join(map(str, row)) + ' |\n'
    sequences = [r for r in records.values() if r['kind'] == 'sequence']
    for seq in sequences:
        coverage += '\n## ' + seq['label'] + '\n\n' + seq['ordering_meaning'] + '\n'
        for pos, title in sorted(seq['positions'].items(), key=lambda x: int(x[0])):
            coverage += '\n### Stage ' + pos + ' ' + title + '\n\n'
            for r in knowledge:
                if any(m['scheme'] == seq['id'] and int(pos) in m['positions'] for m in r.get('sequences', [])):
                    coverage += '- ' + link(r) + '\n'
    out['COVERAGE.md'] = coverage
    inter = opening('Representation interfaces', 'Interfaces connect specified representations through scoped claims, not arbitrary domain arrows.')
    inter += '\n| Interface | Source representation | Predicate | Target representation | Evidence |\n|---|---|---|---|---|\n'
    for r in interfaces:
        m = r['mapping']
        inter += f'| {link(r)} | {records[m["source"]]["label"]} | {m["predicate"]} | {records[m["target"]]["label"]} | {r["evidence_status"]} |\n'
    inter += '\n## Limits and next interfaces\n\nMappings are not a processing staircase. Cardinalities remain unspecified unless explicitly justified. Syntax–prosody, pragmatics–discourse and orthography-related mappings require additional scoped models; the present list is not exhaustive.\n'
    out['INTERFACES.md'] = inter
    queue = opening('Claim and evidence review queue', 'Migration creates no newly verified linguistic claims.')
    queue += '\n## Claim coverage\n\nKey takeaways are exposed as versioned summary claims, not assumed to be atomic propositions. Other body assertions remain unextracted. Context-only evidence records are not claim support.\n'
    queue += '\n| Entity | Extracted claims | Source links | Next task |\n|---|---:|---:|---|\n'
    for r in knowledge:
        queue += f'| {link(r)} | {len(r["claims"])} | {len(targets(r, "kps:cites"))} | Decompose body claims; inspect relevant passages and counterexamples; independent review pending |\n'
    out['REVIEW-QUEUE.md'] = queue
    sources = opening('Source register', 'Source identity and recorded inspection extent do not imply support for every linked assertion.')
    for r in sorted((x for x in records.values() if x['kind'] == 'source'), key=lambda r: r['label']):
        sources += f'\n## {r["label"]}\n\n{link(r)}\n\nRecorded access extent: {r["access_extent"]}\n'
    out['SOURCES.md'] = sources
    return out


def build(root: Path, check: bool = False) -> list[str]:
    result = validate(root, check_views=False)
    if not result['ok']:
        raise ValueError('invalid canonical data: ' + dump(result['errors']))
    stale = []
    for name, text in generated(root).items():
        p = root / name
        if check:
            if not p.exists() or p.read_text(encoding='utf-8') != text:
                stale.append(name)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding='utf-8')
    return stale


def query(root: Path, domain=None, role=None, interfaces=False, ident=None, claim=None) -> list[dict]:
    records, paths = load(root)
    aliases = {a: i for i, r in records.items() for a in r.get('aliases', [])}
    if ident:
        ident = aliases.get(ident, ident)
        if ident not in records:
            raise ValueError('unknown entity or alias: ' + ident)
        return [dict(records[ident], record_path=paths[ident])]
    if domain and (domain not in records or records[domain]['kind'] != 'domain'):
        raise ValueError('unknown domain: ' + domain)
    if role and (role not in records or records[role]['kind'] != 'role'):
        raise ValueError('unknown role: ' + role)
    if claim:
        claim = aliases.get(claim, claim)
        if claim not in records or records[claim]['kind'] != 'claim':
            raise ValueError('unknown claim: ' + claim)
        return [r for _, r in sorted(records.items()) if r['kind'] == 'evidence' and r['about'] == claim]
    return [dict(r, record_path=paths[i]) for i, r in sorted(records.items())
            if r['kind'] in KNOWLEDGE and (not domain or domain in r['domains'])
            and (not role or role in r['roles']) and (not interfaces or r['kind'] == 'interface')]


def cli(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    sub = ap.add_subparsers(dest='command', required=True)
    sub.add_parser('validate')
    b = sub.add_parser('build'); b.add_argument('--check', action='store_true')
    q = sub.add_parser('query')
    for name in ('domain', 'role', 'id', 'claim'):
        q.add_argument('--' + name)
    q.add_argument('--interfaces', action='store_true')
    args = ap.parse_args(argv)
    try:
        if args.command == 'validate':
            result = validate(args.root)
            print(dump(result), end='')
            return 0 if result['ok'] else 1
        if args.command == 'build':
            stale = build(args.root, args.check)
            print(dump({'ok': not stale, 'stale': stale}), end='')
            return bool(stale)
        print(dump(query(args.root, args.domain, args.role, args.interfaces, args.id, args.claim)), end='')
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print('KPS 12 error: ' + str(exc), file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(cli())
