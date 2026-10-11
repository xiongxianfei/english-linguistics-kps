"""One-time, branch-only extraction of the authored draft and pinned KPS tools."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import hashlib
import json
import lzma
import os
import platform
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PIN = '60972c57199ae8bc21d4b7a00ac55552b4105277'
UPSTREAM = 'https://raw.githubusercontent.com/xiongxianfei/knowledge-practice-system/' + PIN + '/'
BLOBS = {'AUTHORING.md':'d5890f789418d4ecf21917add2a9a8915be28d06', 'validate.py':'b9f853f0b6c62d1c9b50839dc45324badc885f73', 'test_validate.py':'de1cd80c477fc71cd69c1863378fd2767ec687f8', 'LICENSE':'f2069d6cff77823390bd06ee0513c324db216050'}
SHA = '3653f8e2f1349430ba4c3e0167a89e525e9fcfed289aa12ab135757852e07960'
RAW_SHA = '8184bf8310e348dd27fa8e6839800e336cd6758ead5d4b29780b35d528e3e06b'
TOP = {'concepts','principles','models','methods','practices','references','tools','tests','data','.github'}
ROOT_FILES = {'README.md','SCOPE.md','COMPATIBILITY.md','CHECKS.md','CONTRIBUTING.md','AGENTS.md','NOTICE.md','NAVIGATION.md','TEMPLATES.md','CHANGELOG.md','REVIEW.md','publication.json','upstream-lock.json','.gitignore'}

os.chdir(ROOT)
blob = b''.join((ROOT/'.bootstrap'/('payload%d.part'%i)).read_bytes() for i in range(7))
if hashlib.sha256(blob).hexdigest()!=SHA:
    raise SystemExit('Compressed payload integrity failure')
raw = lzma.decompress(blob)
if hashlib.sha256(raw).hexdigest()!=RAW_SHA:
    raise SystemExit('Authored payload integrity failure')
payload = json.loads(raw)
if payload.get('format')!=1 or len(payload.get('files',{}))!=136:
    raise SystemExit('Unexpected payload format or file count')
for name,content in payload['files'].items():
    path=PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or not path.parts or '\\' in name:
        raise SystemExit('Unsafe payload path: '+name)
    if (len(path.parts)==1 and name not in ROOT_FILES) or (len(path.parts)>1 and path.parts[0] not in TOP):
        raise SystemExit('Unexpected payload path: '+name)
    target=ROOT.joinpath(*path.parts)
    if target.is_symlink() or any(p.is_symlink() for p in target.parents if p!=ROOT.parent):
        raise SystemExit('Symlink path rejected: '+name)
    if name.startswith('.github/workflows/'):
        if name!='.github/workflows/checks.yml' or not target.is_file() or target.read_text(encoding='utf-8')!=content:
            raise SystemExit('Payload must not change workflows')
        continue
    if not isinstance(content,str):
        raise SystemExit('Payload is not UTF-8 text')
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(content,encoding='utf-8')
print('Extracted 136 authored files after integrity checks',flush=True)
# Correct a document-format issue reported by the unchanged upstream checker.
# Linguistic bracketing is an example, not an application-specific wikilink.
compound=ROOT/'concepts/compounding.md'
text=compound.read_text(encoding='utf-8')
old='a useful hierarchy is [[school [teach-er]]-s].'
if text.count(old)!=1:
    raise SystemExit('Unexpected compound example while applying reviewed format correction')
compound.write_text(text.replace(old,'a useful hierarchy is `[[school [teach-er]]-s]`.'),encoding='utf-8')
lock=json.loads((ROOT/'upstream-lock.json').read_text())
if lock['commit']!=PIN or lock['copied_files']!=BLOBS:
    raise SystemExit('Upstream lock mismatch')
for name,expected in BLOBS.items():
    for attempt in range(3):
        try:
            req=urllib.request.Request(UPSTREAM+name,headers={'User-Agent':'English-KPS-Initial-Build'})
            with urllib.request.urlopen(req,timeout=30) as response:
                data=response.read()
            actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            if actual!=expected:
                raise RuntimeError('Pinned Git blob mismatch: '+name)
            (ROOT/name).write_bytes(data)
            print('Pinned upstream file verified: '+name,flush=True)
            break
        except Exception:
            if attempt==2:raise
            time.sleep(2*(attempt+1))

results=[]
def run(args):
    result=subprocess.run([sys.executable]+args,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print('$ python3 '+' '.join(args),flush=True)
    print(result.stdout,flush=True)
    results.append({'command':['python3']+args,'exit_code':result.returncode,'output':result.stdout})
    if result.returncode:
        raise SystemExit(result.returncode)
    return result.stdout

run(['tools/build_navigation.py'])
# Initial baseline after AI-assisted authoring review of local summaries and
# source limits, not an independent scientific approval or an ordinary CI refresh.
run(['validate.py','.','--accept-reviewed-summaries'])
run(['validate.py','.'])
run(['test_validate.py'])
run(['tools/check_domain.py'])
run(['tools/build_navigation.py','--check'])
run(['-m','unittest','discover','-s','tests','-v'])
validation=json.loads(run(['validate.py','.','--json']))
evidence={'recorded_at':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'build_input_commit':os.environ.get('GITHUB_SHA'),'upstream_commit':PIN,'scope':'Publication structure and constructed-model consistency only; not linguistic truth','scientific_review':'No independent scientific review performed','initial_summary_review':'AI-assisted authoring review of linked summaries and source scope; not expert approval','format_corrections':['Compounding bracket example marked as inline code after initial validation failure'],'validation':validation,'executed_checks':results}
(ROOT/'validation-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('All executed checks passed; evidence recorded; scientific status remains provisional',flush=True)
