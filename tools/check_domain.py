#!/usr/bin/env python3
"""Domain publication invariants; deliberately not a validator of linguistic truth."""
import json, pathlib, re, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import validate as kps

def inspect(root):
    root=pathlib.Path(root); errors=[]; seen=set(); stages=set(); count=0
    for role in sorted(kps.CORE):
        for p in sorted((root/(role+'s')).glob('*.md')):
            try:d=kps.parse(p)
            except Exception as e:errors.append(f'{p.name}: {e}');continue
            if d.meta.get('type')!=role:continue
            count+=1;m=d.meta
            for key in ['id','type','version','language','status','evidence_status','basis_kind','reviewed']:
                if key not in m:errors.append(f'{p.name}: missing {key}')
            if m.get('id') in seen:errors.append(f'{p.name}: duplicate identity')
            seen.add(m.get('id'))
            if m.get('evidence_status')=='provisional':
                if 'provisional' not in kps.section(d,'Evidence status').lower():errors.append(f'{p.name}: provisional status not visible in body')
                if m.get('reviewed') is not None:errors.append(f'{p.name}: provisional item claims reviewed date')
            elif m.get('evidence_status')=='reviewed':
                records=m.get('review_records',[])
                if not records or not all(isinstance(x,str) and (root/x).is_file() for x in records):errors.append(f'{p.name}: reviewed without review record')
            else:errors.append(f'{p.name}: unsupported evidence status')
            if not kps.section(d,'Summary').strip():errors.append(f'{p.name}: empty summary')
            if role in {'concept','principle','model'} and not ('limit' in d.live.lower()):errors.append(f'{p.name}: missing scope limits')
    systems={kps.parse(p).meta.get('system_domain') for p in (root/'models').glob('english-*-system.md')}
    expected={'phonetics','phonology','morphology','lexicon','syntax','semantics','pragmatics','discourse','information-structure','prosody'}
    if systems!=expected:errors.append('Ten subsystem Models are required for this foundation')
    for folder in ('entities','ontology','sequences','views','sources','generated'):
        if (root/folder).exists():errors.append('Abandoned storage layer: '+folder)
    for p in sorted((root/'references').glob('*.md')):
        d=kps.parse(p)
        if d.meta.get('type')!='reference':continue
        for key in ['creator','publication','publication_date','date_basis','accessed','access_extent']:
            if key not in d.meta:errors.append(f'{p.name}: missing reference {key}')
        if not kps.section(d,'Nonclaims'):errors.append(f'{p.name}: missing source nonclaims')
    pub=json.loads((root/'publication.json').read_text())
    if pub.get('scientific_status')!='provisional':errors.append('Initial release must remain explicitly provisional')
    workflow=root/'.github/workflows/checks.yml'
    if workflow.exists() and 'contents: write' in workflow.read_text():errors.append('Permanent CI must not have contents write permission')
    return errors, count

def main():
    errors,count=inspect(ROOT)
    for e in errors:print(e)
    print(f'Domain publication checks: {count} knowledge objects; {len(errors)} errors; no factual certification')
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
