#!/usr/bin/env python3
"""Publication-only checks for the KPS practical Markdown profile.

Python 3.9+ standard library. This is NOT a general YAML/Markdown parser,
scientific validator, competence assessment, or REM project-instance validator.
The authored profile uses JSON-compatible single-line YAML values, ATX headings,
ordinary inline links, and fenced code examples. Code examples are not live links.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import unquote, urlsplit

CORE = {"concept", "principle", "model", "method", "practice"}
FOLDERS = {k: k + 's' for k in CORE}
RELATIONS = {"uses_concepts":"concept", "uses_principles":"principle", "uses_models":"model", "uses_methods":"method", "uses_practices":"practice", "composes":"practice", "references":"reference", "related_knowledge":None}
HEADING = re.compile(r'^(#{1,6})[ \t]+(.+?)[ \t]*$', re.M)
SIMPLE = re.compile(r'^[A-Za-z0-9]+(?: [A-Za-z0-9]+)*$')
LINK = re.compile(r'!?\[(?:[^\]\\\n]|\\.)*\]\(\s*(?:<([^>\n]+)>|([^\s()]+))(?:\s+["\'][^\n]*?["\'])?\s*\)')
IMPERATIVE = re.compile(r'^(?:keep|use|preserve|ensure|always|never|do not|must|shall|require|avoid|make|store|separate)\b', re.I)

@dataclass
class Document:
    path: Path
    meta: dict[str, Any]
    body: str
    live: str
    headings: list[tuple[int, str]]
    links: list[str]

    @property
    def fragments(self) -> set[str]:
        return {slug(t) for _,t in self.headings}

def slug(title: str) -> str:
    return title.lower().replace(' ', '-')

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

MANIFEST_IGNORED_PARTS = frozenset({'.git', '__pycache__', '.pytest_cache'})

def manifest_payload_files(root: Path) -> list[Path]:
    """Publication payload shared by manifest generation and verification.

    Exclude Git internals and tool caches, but retain ordinary repository
    content (including .github, .gitignore, LICENSE and knowledge files).
    """
    return sorted(
        path for path in root.rglob('*')
        if path.is_file()
        and path.name != 'MANIFEST.sha256'
        and not MANIFEST_IGNORED_PARTS.intersection(path.relative_to(root).parts)
    )

def split_frontmatter(text: str) -> tuple[dict[str,Any],str]:
    if not text.startswith('---\n'):
        return {},text
    end=text.find('\n---\n',4)
    if end<0: raise ValueError('unterminated frontmatter')
    meta={}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith('#'):continue
        if ':' not in line:raise ValueError('metadata must use one key per line')
        key,value=line.split(':',1);key=key.strip()
        if key in meta:raise ValueError('duplicate metadata key '+key)
        if not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_-]*',key):raise ValueError('invalid metadata key')
        try:meta[key]=json.loads(value.strip())
        except json.JSONDecodeError as exc:raise ValueError('metadata values must be JSON-compatible YAML: '+key) from exc
    return meta,text[end+5:]

def live_markdown(body: str) -> str:
    """Hide fenced/indented code and inline code, preserving line positions."""
    output=[]; fence=None; width=0
    for line in body.splitlines():
        m=re.match(r'^ {0,3}(`{3,}|~{3,})',line)
        if fence:
            if m and m[1][0]==fence and len(m[1])>=width and not line[m.end():].strip():fence=None
            output.append('');continue
        if m:
            fence=m[1][0];width=len(m[1]);output.append('');continue
        if line.startswith('    ') or line.startswith('\t'):
            output.append('');continue
        output.append(line)
    text='\n'.join(output)
    return re.sub(r'(`+)([^`\n]*(?:`(?!`)[^`\n]*)*)\1', '',text)

def parse(path: Path) -> Document:
    meta,body=split_frontmatter(path.read_text(encoding='utf-8'))
    live=live_markdown(body)
    hs=[(len(m[1]),m[2]) for m in HEADING.finditer(live)]
    links=[m[1] or m[2] for m in LINK.finditer(live)]
    return Document(path,meta,body,live,hs,links)

def section(doc: Document, pattern: str) -> str:
    match=re.search(r'^## '+pattern+r'\s*$',doc.live,re.M|re.I)
    if not match:return ''
    end=re.search(r'^## ',doc.live[match.end():],re.M)
    return doc.live[match.end():match.end()+end.start()] if end else doc.live[match.end():]

def meaningful(text: str) -> str:
    # Strip destinations and formatting; retain link labels for normal prose.
    return re.sub(r'\s+',' ',LINK.sub('',text).replace('*','').strip())

def resolve(root:Path,source:Path,destination:str) -> tuple[Path,str] | None:
    u=urlsplit(destination)
    if u.scheme or u.netloc:return None
    if u.query:raise ValueError('local query strings are outside this profile')
    name=unquote(u.path)
    if name.startswith(('/', '\\')):raise ValueError('absolute local path')
    target=(source.parent/name).resolve() if name else source.resolve()
    try:target.relative_to(root.resolve())
    except ValueError as exc:raise ValueError('target escapes package') from exc
    return target,unquote(u.fragment)

def snapshot(root:Path,docs:dict[Path,Document],byid:dict[str,Document]) -> dict[str,Any]:
    entries={}
    for path,doc in docs.items():
        if doc.meta.get('type') not in CORE|{'reference'}:continue
        targets=set()
        for dest in doc.links:
            try:r=resolve(root,path,dest)
            except ValueError:continue
            if r and r[0] in docs and docs[r[0]].meta.get('type') in CORE|{'reference'} and r[0]!=path:targets.add(r[0])
        for key in RELATIONS:
            for ident in doc.meta.get(key,[]) if isinstance(doc.meta.get(key,[]),list) else []:
                if ident in byid and byid[ident].path!=path:targets.add(byid[ident].path)
        if targets:
            entries[path.relative_to(root).as_posix()]={p.relative_to(root).as_posix():sha(p) for p in sorted(targets)}
    return {'format':1,'meaning':'Declared/direct dependencies requiring human summary review after content changes; not proof of factual or semantic validity.','entries':entries}

def validate(root: Path, manifest: bool=False, refresh: bool=False) -> dict[str,Any]:
    root=root.resolve();errors=[];docs={};byid={};relations=0;local_links=0;stage_count=0
    def error(code:str,path:Path|str,detail:str):errors.append({'code':code,'file':str(path.relative_to(root)) if isinstance(path,Path) else path,'detail':detail})
    try:pub=json.loads((root/'publication.json').read_text())
    except (OSError,ValueError):pub={};error('publication','publication.json','missing or invalid publication metadata')
    if pub.get('kps_language')!='9.x':error('compatibility','publication.json','expected major-line 9.x, not an exact-version dependency')
    if not re.fullmatch(r'9\.\d+\.\d+',str(pub.get('validated_with',''))):error('compatibility','publication.json','exact inspected authoring release must be recorded separately')
    if pub.get('markdown_profile')!='practical-markdown-v1':error('profile','publication.json','wrong Markdown profile')
    for folder in [*FOLDERS.values(),'references']:
        if not (root/folder).is_dir():error('folder',folder,'missing required knowledge/reference folder')
    for path in sorted(root.rglob('*.md')):
        if '.github' in path.relative_to(root).parts:
            continue  # Hosting infrastructure, not KPS knowledge documents.
        try:doc=parse(path)
        except (OSError,UnicodeError,ValueError) as exc:error('parse',path,str(exc));continue
        docs[path]=doc
        m=doc.meta;typ=m.get('type')
        if m.get('language')!='KPS 9.x':error('language',path,'missing or inconsistent language declaration')
        if sum(n==1 for n,h in doc.headings)!=1:error('h1',path,'exactly one document title is required')
        counts=Counter(h for n,h in doc.headings)
        for h,c in counts.items():
            if c>1:error('duplicate-heading',path,h)
            if not SIMPLE.fullmatch(h):error('heading-profile',path,h)
        for wanted in ('Key takeaway','Summary'):
            if not any(h==wanted for n,h in doc.headings):error('local-summary',path,'missing '+wanted)
            elif not meaningful(section(doc,re.escape(wanted))):error('local-summary',path,'empty '+wanted)
        if re.search(r'<\s*a\b[^>]*\b(?:id|name)\s*=',doc.live,re.I):error('html-anchor',path,'custom HTML anchor is outside this profile')
        if re.search(r'\[\[[^\]]+\]\]',doc.live):error('wikilink',path,'application-specific wikilink')
        ident=m.get('id')
        if ident:
            if ident in byid:error('duplicate-id',path,str(ident))
            else:byid[ident]=doc
        relative=path.relative_to(root)
        if relative.parts[0] in set(FOLDERS.values()) and path.name!='README.md':
            if typ not in CORE or FOLDERS.get(typ)!=relative.parts[0]:error('type-folder',path,str(typ))
        if typ in CORE|{'reference'} and not ident:error('missing-id',path,'knowledge/reference file needs an identity')
        if typ=='reference':
            if relative.parts[0]!='references':error('type-folder',path,'reference outside supporting folder')
            if not any(urlsplit(x).scheme in ('https','http') for x in doc.links):error('reference-url',path,'no external publication link')
            if not m.get('access_extent'):error('reference-access',path,'inspected extent missing')
        if typ=='principle':
            title=next((h for n,h in doc.headings if n==1),'')
            statement=meaningful(section(doc,'Statement'))
            if IMPERATIVE.match(title) or (statement and IMPERATIVE.match(statement)):error('imperative-principle',path,'title/statement appears to prescribe rather than explain; heuristic review only')
        if typ=='method':
            hs=' '.join(h.lower() for n,h in doc.headings)
            if not ('rationale' in hs or 'why this operation' in hs):error('method-rationale',path,'no local rationale section')
            if not ('steps' in hs or 'procedure' in hs):error('method-procedure',path,'no procedure')
            if 'inputs' not in hs and 'prerequisites' not in hs:error('method-inputs',path,'no local inputs/prerequisites')
            if not ('limits' in hs or 'counterevidence' in hs):error('method-limits',path,'missing limits')
            if not ('validation' in hs or 'checks' in hs or 'counterevidence' in hs):error('method-validation',path,'no output/evaluation check')
        if typ=='practice':
            stage_matches=list(re.finditer(r'^## (Stage(\d+) (.+))$',doc.live,re.M))
            if not stage_matches:error('practice-stages',path,'no StageN execution stages')
            nums=[int(x[2]) for x in stage_matches]
            if nums!=list(range(1,len(nums)+1)):error('stage-order',path,'StageN sequence has a gap, duplicate or incorrect order')
            titles=[x[1] for x in stage_matches]
            if m.get('stage_titles')!=titles:error('stage-metadata',path,'stage_titles differs from actual heading order')
            if 'recommended' not in doc.live.lower() or 'prerequisite' not in doc.live.lower():error('stage-meaning',path,'order/dependency distinction absent')
            for match in stage_matches:
                next_h=re.search(r'^## ',doc.live[match.end():],re.M)
                body=doc.live[match.end():match.end()+next_h.start()] if next_h else doc.live[match.end():]
                for label in ('Goal','Why','What to do','What to observe','Success signal','Next'):
                    lm=re.search(r'\*\*'+re.escape(label)+r':\*\*\s*(.+)',body)
                    if not lm or not meaningful(lm[1]):error('stage-local-card',path,match[1]+': missing or link-only '+label)
                if 'procedure' not in body.lower():error('stage-procedure',path,match[1]+': no inline procedure')
                if len(meaningful(body).split())<65:error('stage-thin',path,match[1]+': inspect insufficient local content (heuristic)')
                if '#'+slug(match[1]) not in doc.links:error('stage-navigation',path,match[1]+': no live stage-map link')
            stage_count+=len(stage_matches)
    graph={}
    for path,doc in docs.items():
        for key,target_type in RELATIONS.items():
            vals=doc.meta.get(key,[])
            if not isinstance(vals,list):error('relationship-format',path,key);continue
            for ident in vals:
                relations+=1
                if ident not in byid:error('unresolved-id',path,key+': '+str(ident));continue
                actual=byid[ident].meta.get('type')
                if target_type and actual!=target_type:error('relationship-type',path,key+': '+str(ident))
                if not target_type and actual not in CORE:error('relationship-type',path,key+' expects core knowledge: '+str(ident))
            if key=='composes':graph[doc.meta.get('id','')]=vals
        for dest in doc.links:
            try:r=resolve(root,path,dest)
            except ValueError as exc:error('local-link',path,dest+': '+str(exc));continue
            if r is None:continue
            target,frag=r;local_links+=1
            if not target.is_file():error('missing-target',path,dest);continue
            if frag:
                if target.suffix.lower()!='.md' or target not in docs:error('fragment-target',path,dest)
                elif frag not in docs[target].fragments:error('missing-fragment',path,dest)
    def walk(node,stack,done):
        if node in stack:raise ValueError(' -> '.join([*stack,node]))
        if node in done:return
        for nxt in graph.get(node,[]):walk(nxt,[*stack,node],done)
        done.add(node)
    try:
        done=set()
        for node in graph:walk(node,[],done)
    except ValueError as exc:error('composition-cycle','metadata',str(exc))
    expected=snapshot(root,docs,byid)
    sf=root/'summary-dependencies.json'
    if refresh and not errors:sf.write_text(json.dumps(expected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if sf.exists():
        try:old=json.loads(sf.read_text())
        except ValueError:old={};error('summary-snapshot',sf,'invalid JSON')
        oldentries=old.get('entries',{})
        for name,deps in expected['entries'].items():
            olddeps=oldentries.get(name,{})
            if olddeps!=deps:error('stale-summary',name,'declared/direct dependencies changed; review then refresh, do not blindly accept')
        for name in oldentries.keys()-expected['entries'].keys():error('stale-summary',name,'recipient removed or dependencies changed')
    elif not refresh:error('summary-snapshot','summary-dependencies.json','missing reviewed dependency snapshot')
    manifest_files=0
    if manifest:
        mf=root/'MANIFEST.sha256'
        if not mf.is_file():error('manifest',mf,'missing')
        else:
            named=set()
            for line in mf.read_text().splitlines():
                try:digest,name=line.split('  ',1)
                except ValueError:error('manifest',mf,'invalid line');continue
                p=(root/name).resolve()
                try:p.relative_to(root)
                except ValueError:error('manifest',mf,'path escapes');continue
                named.add(name);manifest_files+=1
                if not p.is_file() or sha(p)!=digest:error('manifest-hash',name,'missing file or checksum mismatch')
            actual={p.relative_to(root).as_posix() for p in manifest_payload_files(root)}
            if actual!=named:error('manifest-coverage','MANIFEST.sha256','listed/actual payload sets differ')
    types=Counter(d.meta.get('type','document') for d in docs.values())
    stats={'markdown_documents':len(docs),'knowledge_objects':sum(types[x] for x in CORE),'reference_records':types['reference'],'by_type':{k:types[k] for k in sorted(CORE)},'local_links':local_links,'typed_relationships':relations,'practice_stages':stage_count,'heading_identifiers':sum(len(d.headings) for d in docs.values()),'summary_recipients':len(expected['entries']),'summary_dependencies':sum(map(len,expected['entries'].values())),'manifest_files':manifest_files}
    return {'ok':not errors,'scope':'publication structure and declared dependency changes only; not factual or domain conformance validation','stats':stats,'errors':errors}

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('root',nargs='?',default='.')
    ap.add_argument('--manifest',action='store_true')
    ap.add_argument('--accept-reviewed-summaries',action='store_true',help='Refresh dependency hashes only after actual human/content review; not a truth certificate')
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    result=validate(Path(args.root),args.manifest,args.accept_reviewed_summaries)
    if args.json:print(json.dumps(result,indent=2))
    else:
        print('PASS' if result['ok'] else 'FAIL',json.dumps(result['stats']))
        for e in result['errors']:print(f"{e['code']}: {e['file']}: {e['detail']}")
    return 0 if result['ok'] else 1
if __name__=='__main__':sys.exit(main())
