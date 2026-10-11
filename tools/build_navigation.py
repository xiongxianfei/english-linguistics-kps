#!/usr/bin/env python3
"""Generate navigation and review views from canonical Markdown metadata; no snapshot refresh."""
import argparse, collections, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate as kps
STAGES = {0:'Foundations',1:'Morphology and Lexicon',2:'Syntax',3:'Semantics',4:'Pragmatics',5:'Discourse and Information Structure',6:'Phonetics and Phonology',7:'Interfaces and Integration'}
ROLES = ['concept','principle','model','method','practice']
def opening(title, takeaway):
    return '---\nlanguage: "KPS 9.x"\npackage_version: "0.1.0"\nstatus: "draft"\n---\n\n# '+title+'\n\n## Key takeaway\n'+takeaway+'\n\n## Summary\nGenerated navigation over canonical knowledge objects. Stage labels record coverage, not empirical mastery or KPS knowledge roles. All linguistic content in this initial release is provisional.\n'
def collect():
    out=[]
    for role in ROLES:
        for p in sorted((ROOT/(role+'s')).glob('*.md')):
            d=kps.parse(p)
            if d.meta.get('type')==role:
                title=next(h for n,h in d.headings if n==1)
                out.append((p.relative_to(ROOT).as_posix(),title,d.meta))
    return out

def generated():
    docs=collect()
    index=opening('Knowledge index','Browse by KPS role, then follow typed relationships and local source summaries.')
    for role in ROLES:
        index+='\n## '+role.capitalize()+'s\n\n'
        for path,title,m in docs:
            if m['type']==role:index+=f'- [{title}]({path}) — Stage {", ".join(map(str,m["stages"]))}; provisional.\n'
    index+='\n## Other views\n\n[Stage coverage](COVERAGE.md), [source register](references/README.md), [review queue](REVIEW-QUEUE.md), and [interface map](models/english-system-architecture.md).\n'
    coverage=opening('Stage coverage','Stages 0 through 7 are a navigational view over reusable KPS objects, not eight duplicate knowledge hierarchies.')
    for n,title in STAGES.items():
        coverage+=f'\n## Stage {n} {title}\n\n'
        for path,t,m in docs:
            if n in m['stages']:coverage+=f'- [{t}]({path}) ({m["type"]}; provisional)\n'
    coverage+='\n## Coverage limits\n\nCoverage is broad introductory coverage, not a complete English grammar, validated curriculum or evidence of learner proficiency. Research on varieties, corpus frequency, acquisition, historical change and detailed formal derivations remains outside this first draft.\n'
    queue=opening('Scientific review queue','Every initial linguistic object remains provisional and needs independent claim level review.')
    queue+='\n## Review priorities\n\nPrioritize theory-sensitive analyses, accent-sensitive phonetics, generalized negation and scope claims, and source gaps. Bibliographic existence, selected-source inspection and full claim verification are different statuses. A source-backed definition can coexist with unverified examples and explanations in the same note.\n\n## Objects awaiting review\n\n| Object | Role | Source status | Next evidence task |\n|---|---|---|---|\n'
    for path,t,m in docs:
        source_status='Selected source support only' if m.get('references') else 'No external support linked yet'
        queue+=f'| [{t}]({path}) | {m["type"]} | {source_status} | Inspect claim-specific evidence and counterexamples; independent review pending |\n'
    queue+='\n## Promotion criterion\n\nA status change requires a review record naming the inspected passages, supported claim, scope, counterevidence and actual reviewer. No independent review has occurred in this initial draft. The authoring assistant\'s checks are not external scientific approval.\n'
    graph={'format':1,'description':'Generated typed dependency graph, not a causal model of the brain.','nodes':[{'id':m['id'],'type':m['type'],'path':p,'stages':m['stages']} for p,t,m in docs],'edges':[]}
    for p,t,m in docs:
        for key in kps.RELATIONS:
            for target in m.get(key,[]):graph['edges'].append({'source':m['id'],'relationship':key,'target':target})
    for p in sorted((ROOT/'references').glob('*.md')):
        d=kps.parse(p)
        if d.meta.get('type')=='reference':graph['nodes'].append({'id':d.meta['id'],'type':'reference','path':p.relative_to(ROOT).as_posix()})
    return {'INDEX.md':index,'COVERAGE.md':coverage,'REVIEW-QUEUE.md':queue,'knowledge-graph.json':json.dumps(graph,ensure_ascii=False,indent=2)+'\n'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args()
    stale=[]
    for name,text in generated().items():
        path=ROOT/name
        if a.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=text:stale.append(name)
        else:path.write_text(text,encoding='utf-8')
    if stale:print('Stale generated views: '+', '.join(stale));return 1
    print('Navigation views checked' if a.check else 'Navigation views written');return 0
if __name__=='__main__':raise SystemExit(main())
