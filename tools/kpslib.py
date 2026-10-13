#!/usr/bin/env python3
"""Core parser, validator and deterministic view compiler for the KPS 12 foundation."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from collections import Counter, defaultdict
from urllib.parse import urlsplit
import hashlib
import json
import os
import re

ROLES = ("concept", "principle", "model", "method", "practice")
ROLE_FOLDERS = {role: role + "s" for role in ROLES}
FOLDER_ROLES = {folder: role for role, folder in ROLE_FOLDERS.items()}
FORBIDDEN_DIRS = {"entities", "ontology", "knowledge", "references"}
ID_RE = re.compile(r"^[a-z][a-z0-9]*(?::[a-z0-9][a-z0-9-]*)+$")
TERM_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*(?::[a-z][a-z0-9]*(?:-[a-z0-9]+)*)*$")
PREDICATE_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.M)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

ROLE_SECTIONS = {
    "concept": ("Definition", "Distinctions", "Scope and limits"),
    "principle": ("Statement", "Explanation", "Scope and counterevidence"),
    "model": ("Purpose", "Representation", "Assumptions and limits", "Evaluation and counterevidence"),
    "method": (
        "Objective", "Inputs and prerequisites", "Rationale", "Procedure", "Expected effect",
        "Validation and counterevidence", "Limits",
    ),
    "practice": (),
}

@dataclass(frozen=True)
class Document:
    path: Path
    relpath: str
    role: str | None
    kind: str
    meta: dict[str, Any]
    body: str
    title: str
    headings: tuple[tuple[int, str], ...]
    links: tuple[str, ...]

    def section(self, name: str) -> str:
        pattern = re.compile(rf"^## {re.escape(name)}\s*$\n(.*?)(?=^## |\Z)", re.M | re.S)
        match = pattern.search(self.body)
        return match.group(1).strip() if match else ""

    @property
    def key_takeaway(self) -> str:
        return " ".join(line.strip() for line in self.section("Key takeaway").splitlines() if line.strip())


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing JSON-compatible YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    raw = text[4:end]
    meta: dict[str, Any] = {}
    for number, line in enumerate(raw.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"frontmatter line {number} lacks ':'")
        key, value = line.split(":", 1)
        key = key.strip()
        if key in meta:
            raise ValueError(f"duplicate metadata key {key}")
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", key):
            raise ValueError(f"invalid metadata key {key}")
        try:
            meta[key] = json.loads(value.strip())
        except json.JSONDecodeError as exc:
            raise ValueError(f"metadata value must be JSON-compatible: {key}") from exc
    return meta, text[end + 5 :]


def slug(text: str) -> str:
    text = re.sub(r"[`*_]", "", text.strip().lower())
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text).strip("-")


def parse_document(path: Path, root: Path) -> Document:
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    headings = tuple((len(m.group(1)), m.group(2).strip()) for m in HEADING_RE.finditer(body))
    titles = [h for level, h in headings if level == 1]
    if len(titles) != 1:
        title = titles[0] if titles else path.stem.replace("-", " ").title()
    else:
        title = titles[0]
    role = FOLDER_ROLES.get(path.parent.name)
    kind = "knowledge" if role else path.parent.name.removesuffix("s")
    links = tuple(m.group(2) for m in LINK_RE.finditer(body))
    return Document(path, path.relative_to(root).as_posix(), role, kind, meta, body, title, headings, links)


def collect(root: Path) -> list[Document]:
    docs: list[Document] = []
    for role, folder in ROLE_FOLDERS.items():
        for path in sorted((root / folder).glob("*.md")):
            docs.append(parse_document(path, root))
    for folder in ("sources", "sequences"):
        for path in sorted((root / folder).glob("*.md")):
            docs.append(parse_document(path, root))
    return docs


def top_domain(domain: str) -> str:
    return domain.split(":", 1)[0]


def domain_label(domain: str) -> str:
    return domain.split(":")[-1].replace("-", " ").title()


def role_label(role: str) -> str:
    return role.replace("-", " ").title()


def normalize_claim_id(owner: str, claim_id: str) -> str:
    return f"{owner}#{claim_id}"


def build_state(root: Path) -> dict[str, Any]:
    docs = collect(root)
    knowledge = [d for d in docs if d.role]
    sources = [d for d in docs if d.kind == "source"]
    sequences = [d for d in docs if d.kind == "sequence"]
    by_id: dict[str, Document] = {}
    aliases: dict[str, str] = {}
    for doc in docs:
        ident = doc.meta.get("id")
        if isinstance(ident, str):
            by_id[ident] = doc
            for alias in doc.meta.get("aliases", []) if isinstance(doc.meta.get("aliases", []), list) else []:
                aliases[alias] = ident

    domain_docs: dict[str, list[Document]] = defaultdict(list)
    relation_uses: dict[str, list[dict[str, Any]]] = defaultdict(list)
    claims: list[dict[str, Any]] = []
    interfaces: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    def edge(source: str, predicate: str, target: str, layer: str, **extra: Any) -> None:
        material = json.dumps([source, predicate, target, layer, extra], ensure_ascii=False, sort_keys=True)
        item = {
            "id": "edge:" + hashlib.sha256(material.encode("utf-8")).hexdigest()[:20],
            "source": source,
            "predicate": predicate,
            "target": target,
            "layer": layer,
        }
        item.update(extra)
        edges.append(item)

    all_domains: set[str] = set()
    for doc in knowledge:
        ident = doc.meta["id"]
        nodes.append({
            "id": ident,
            "kind": "knowledge",
            "role": doc.role,
            "label": doc.title,
            "path": doc.relpath,
            "version": doc.meta.get("version"),
            "status": doc.meta.get("status"),
            "evidence_status": doc.meta.get("evidence_status"),
            "domains": doc.meta.get("domains", []),
        })
        edge(ident, "has-role", f"role:{doc.role}", "classification")
        for domain in doc.meta.get("domains", []):
            all_domains.add(domain)
            domain_docs[domain].append(doc)
            edge(ident, "in-domain", f"domain:{domain}", "classification")
        for claim in doc.meta.get("claims", []):
            cid = normalize_claim_id(ident, claim["id"])
            record = {
                "id": cid,
                "owner": ident,
                "owner_version": doc.meta.get("version"),
                "statement": claim.get("statement"),
                "scope": claim.get("scope"),
                "evidence_status": claim.get("evidence_status"),
                "path": doc.relpath,
            }
            claims.append(record)
            nodes.append({"id": cid, "kind": "claim", "label": claim.get("statement"), "owner": ident})
            edge(ident, "asserts", cid, "claim")
        for relation in doc.meta.get("relations", []):
            record = dict(relation)
            record["source"] = ident
            relation_uses[relation["predicate"]].append(record)
            target = aliases.get(relation["target"], relation["target"])
            extra = {k: v for k, v in relation.items() if k not in {"predicate", "target", "layer"}}
            edge(ident, relation["predicate"], target, relation.get("layer", "semantic"), **extra)
        for source in doc.meta.get("sources", []):
            sid = aliases.get(source["id"], source["id"])
            relation = source.get("relation", "context-only")
            evidence_id = f"evidence:{hashlib.sha256((ident+'|'+sid+'|'+relation).encode()).hexdigest()[:20]}"
            ev = {"id": evidence_id, "owner": ident, "source": sid, **source}
            ev["source"] = sid
            evidence.append(ev)
            nodes.append({"id": evidence_id, "kind": "evidence", "label": f"{relation}: {sid}", "owner": ident})
            edge(evidence_id, relation, ident if relation == "context-only" else normalize_claim_id(ident, source.get("claim", "key-takeaway")), "evidence", evidence_source=sid)
        if doc.meta.get("interface"):
            record = {"id": ident, "label": doc.title, "path": doc.relpath, **doc.meta["interface"]}
            interfaces.append(record)

    for doc in sources:
        ident = doc.meta["id"]
        nodes.append({"id": ident, "kind": "source", "label": doc.title, "path": doc.relpath})
    for domain in sorted(all_domains):
        nodes.append({"id": f"domain:{domain}", "kind": "domain", "label": domain_label(domain), "parent": f"domain:{domain.rsplit(':',1)[0]}" if ":" in domain else None})
        if ":" in domain:
            edge(f"domain:{domain}", "narrower-than", f"domain:{domain.rsplit(':',1)[0]}", "classification")
    for role in ROLES:
        nodes.append({"id": f"role:{role}", "kind": "role", "label": role_label(role)})
    for predicate, uses in sorted(relation_uses.items()):
        nodes.append({"id": f"relation:{predicate}", "kind": "relation-vocabulary", "label": predicate.replace("-", " ").title(), "uses": len(uses)})
    for seq in sequences:
        ident = seq.meta["id"]
        nodes.append({"id": ident, "kind": "sequence", "label": seq.title, "path": seq.relpath})
        for index, stage in enumerate(seq.meta.get("stages", []), 1):
            for member in stage.get("members", []):
                target = aliases.get(member, member)
                edge(target, "in-sequence", ident, "navigation", stage=stage["id"], position=index)

    nodes.sort(key=lambda x: (x["kind"], x["id"]))
    edges.sort(key=lambda x: x["id"])
    claims.sort(key=lambda x: x["id"])
    interfaces.sort(key=lambda x: x["id"])
    evidence.sort(key=lambda x: x["id"])

    return {
        "docs": docs,
        "knowledge": knowledge,
        "sources": sources,
        "sequences": sequences,
        "by_id": by_id,
        "aliases": aliases,
        "domain_docs": domain_docs,
        "relation_uses": relation_uses,
        "claims": claims,
        "interfaces": interfaces,
        "evidence": evidence,
        "nodes": nodes,
        "edges": edges,
        "all_domains": all_domains,
    }


def markdown_header(title: str, takeaway: str) -> str:
    return f"# {title}\n\n## Key takeaway\n{takeaway}\n\n## Summary\nGenerated from canonical KPS 12 Markdown. Views are navigation artifacts, not independent knowledge or scientific review.\n"


def generated_files(root: Path) -> dict[str, str]:
    state = build_state(root)
    knowledge: list[Document] = state["knowledge"]
    publication = json.loads((root / "publication.json").read_text(encoding="utf-8"))
    outputs: dict[str, str] = {}

    # Role views and root index.
    index = markdown_header("Knowledge index", "Browse canonical knowledge by its exclusive primary role.")
    for role in ROLES:
        docs = sorted([d for d in knowledge if d.role == role], key=lambda d: d.title.lower())
        view = markdown_header(role_label(role) + "s", f"Canonical {role} knowledge, classified independently from domain membership.")
        for doc in docs:
            rel = os.path.relpath(root / doc.relpath, root / "views" / "roles").replace(os.sep, "/")
            view += f"- [{doc.title}]({rel}) — {', '.join(doc.meta.get('domains', []))}; {doc.meta.get('evidence_status')}.\n"
        outputs[f"views/roles/{role}s.md"] = view
        index += f"\n## {role_label(role)}s\n\n"
        for doc in docs:
            index += f"- [{doc.title}]({doc.relpath}) — {', '.join(doc.meta.get('domains', []))}; {doc.meta.get('evidence_status')}.\n"
    outputs["INDEX.md"] = index

    # Domain views.
    top_domains = sorted({top_domain(d) for d in state["all_domains"]})
    coverage_view = markdown_header("Domain coverage", "Ten foundation domains and any additional authored classifications are generated from knowledge metadata.")
    coverage_root = markdown_header("Domain coverage", "Ten foundation domains and any additional authored classifications are generated from knowledge metadata.")
    required = publication["foundation_domains"]
    for domain in top_domains:
        docs = sorted({d.relpath: d for key, values in state["domain_docs"].items() if top_domain(key) == domain for d in values}.values(), key=lambda d: d.title.lower())
        subdomains = sorted(x for x in state["all_domains"] if x.startswith(domain + ":"))
        view = markdown_header(domain_label(domain), f"A generated perspective over knowledge classified in {domain.replace('-', ' ')}.")
        view += "\n## Internal structure\n\n"
        if subdomains:
            view += "| Subdomain | Knowledge items |\n|---|---:|\n"
            for sub in subdomains:
                view += f"| {domain_label(sub)} | {len({d.relpath for d in state['domain_docs'][sub]})} |\n"
        else:
            view += "No subdomains have yet been introduced.\n"
        view += "\n## Canonical knowledge\n\n"
        for doc in docs:
            rel = os.path.relpath(root / doc.relpath, root / "views" / "domains").replace(os.sep, "/")
            view += f"- [{doc.title}]({rel}) — {role_label(doc.role or '')}; {doc.meta.get('evidence_status')}.\n"
        intfs = [i for i in state["interfaces"] if domain in {i["source_domain"], i["target_domain"]}]
        if intfs:
            view += "\n## Interfaces\n\n"
            for item in intfs:
                rel = os.path.relpath(root / item["path"], root / "views" / "domains").replace(os.sep, "/")
                view += f"- [{item['label']}]({rel}) — {item['source_domain']} `{item['predicate']}` {item['target_domain']}.\n"
        view += "\n## Evidence boundary\n\nClassification and file count do not establish completeness, consensus or empirical adequacy.\n"
        outputs[f"views/domains/{domain}.md"] = view
        status = "required foundation domain" if domain in required else "additional authored classification"
        line = f"- [{domain_label(domain)}]({{path}}) — {len(docs)} knowledge items; {len(subdomains)} subdomains; {status}.\n"
        coverage_view += line.format(path=f"domains/{domain}.md")
        coverage_root += line.format(path=f"views/domains/{domain}.md")
    outputs["views/coverage.md"] = coverage_view
    outputs["COVERAGE.md"] = coverage_root

    # Relation views.
    for predicate, uses in sorted(state["relation_uses"].items()):
        view = markdown_header(predicate.replace("-", " ").title(), f"Observed authored uses of the open relation predicate `{predicate}`.")
        view += "\n## Uses\n\n"
        for use in sorted(uses, key=lambda x: (x["source"], x["target"])):
            source_doc = state["by_id"].get(use["source"])
            target_id = state["aliases"].get(use["target"], use["target"])
            target_doc = state["by_id"].get(target_id)
            if source_doc and target_doc:
                srel = os.path.relpath(source_doc.path, root / "views" / "relations").replace(os.sep, "/")
                trel = os.path.relpath(target_doc.path, root / "views" / "relations").replace(os.sep, "/")
                view += f"- [{source_doc.title}]({srel}) → [{target_doc.title}]({trel}) — layer `{use.get('layer','semantic')}`.\n"
        outputs[f"views/relations/{predicate}.md"] = view

    # Interface view.
    interfaces = markdown_header("Representation interfaces", "Interface Models connect explicit representation labels through scoped, provisional mappings.")
    interfaces += "\n| Interface | Source | Predicate | Target | Cardinality |\n|---|---|---|---|---|\n"
    for item in state["interfaces"]:
        rel = os.path.relpath(root / item["path"], root / "views").replace(os.sep, "/")
        interfaces += f"| [{item['label']}]({rel}) | {item['source_domain']} / {item['source_representation']} | `{item['predicate']}` | {item['target_domain']} / {item['target_representation']} | {item['cardinality']} |\n"
    interfaces += "\n## Limits\n\nAn interface is an authored Model, not an automatic causal or processing edge. All mappings remain provisional unless their claim evidence says otherwise.\n"
    outputs["views/interfaces.md"] = interfaces

    # Review/evidence view.
    review_view = markdown_header("Review queue", "Every foundational claim remains provisional unless a version-specific review record says otherwise.")
    review_root = markdown_header("Review queue", "Every foundational claim remains provisional unless a version-specific review record says otherwise.")
    header = "\n| Knowledge item | Role | Sources | Evidence status |\n|---|---|---:|---|\n"
    review_view += header
    review_root += header
    for doc in sorted(knowledge, key=lambda d: d.title.lower()):
        view_rel = os.path.relpath(doc.path, root / "views").replace(os.sep, "/")
        root_rel = doc.relpath
        row = f"| [{{title}}]({{path}}) | {{role}} | {{sources}} | {{status}} |\n"
        values = {"title": doc.title, "role": role_label(doc.role or ''), "sources": len(doc.meta.get('sources', [])), "status": doc.meta.get('evidence_status')}
        review_view += row.format(path=view_rel, **values)
        review_root += row.format(path=root_rel, **values)
    boundary = "\n## Boundary\n\nA source count is not a support score. Context-only links retain publication provenance without asserting claim-level support.\n"
    review_view += boundary
    review_root += boundary
    outputs["views/review.md"] = review_view
    outputs["REVIEW-QUEUE.md"] = review_root

    # Sequence views.
    for seq in state["sequences"]:
        view = markdown_header(seq.title, "Generated linked route from the authored Sequence definition.")
        for stage in seq.meta.get("stages", []):
            view += f"\n## {stage['label']}\n\n"
            for member in stage.get("members", []):
                ident = state["aliases"].get(member, member)
                doc = state["by_id"].get(ident)
                if doc:
                    rel = os.path.relpath(doc.path, root / "views" / "sequences").replace(os.sep, "/")
                    view += f"- [{doc.title}]({rel}) — {role_label(doc.role or '')}.\n"
        outputs[f"views/sequences/{seq.path.stem}.md"] = view

    # Machine outputs.
    graph = {
        "format": 12,
        "profile": publication["profile"],
        "description": "Generated from canonical role-based Markdown; no automatic truth, causal, symmetric or transitive inference.",
        "nodes": state["nodes"],
        "edges": state["edges"],
    }
    outputs["generated/knowledge-graph.json"] = json.dumps(graph, ensure_ascii=False, indent=2) + "\n"
    domain_json = []
    for domain in sorted(state["all_domains"]):
        domain_json.append({
            "id": domain,
            "label": domain_label(domain),
            "parent": domain.rsplit(":", 1)[0] if ":" in domain else None,
            "knowledge": sorted({d.meta["id"] for d in state["domain_docs"][domain]}),
        })
    outputs["generated/domains.json"] = json.dumps(domain_json, ensure_ascii=False, indent=2) + "\n"
    relation_json = [
        {"predicate": predicate, "uses": sorted(uses, key=lambda x: (x["source"], x["target"]))}
        for predicate, uses in sorted(state["relation_uses"].items())
    ]
    outputs["generated/relations.json"] = json.dumps(relation_json, ensure_ascii=False, indent=2) + "\n"
    outputs["generated/claims.json"] = json.dumps(state["claims"], ensure_ascii=False, indent=2) + "\n"
    outputs["generated/interfaces.json"] = json.dumps(state["interfaces"], ensure_ascii=False, indent=2) + "\n"
    outputs["generated/evidence.json"] = json.dumps(state["evidence"], ensure_ascii=False, indent=2) + "\n"
    search = [
        {"id": d.meta["id"], "title": d.title, "role": d.role, "domains": d.meta.get("domains", []), "path": d.relpath, "summary": d.section("Summary")}
        for d in sorted(knowledge, key=lambda d: d.meta["id"])
    ]
    outputs["generated/search-index.json"] = json.dumps(search, ensure_ascii=False, indent=2) + "\n"
    manifest = {path: hashlib.sha256(text.encode("utf-8")).hexdigest() for path, text in sorted(outputs.items())}
    outputs["generated/build-manifest.json"] = json.dumps({"profile": publication["profile"], "files": manifest}, indent=2) + "\n"
    return outputs


def write_generated(root: Path) -> list[str]:
    outputs = generated_files(root)
    for folder in (root / "views", root / "generated"):
        if folder.exists():
            for path in sorted(folder.rglob("*"), reverse=True):
                if path.is_file(): path.unlink()
                elif path.is_dir(): path.rmdir()
        folder.mkdir(parents=True, exist_ok=True)
    for rel, text in outputs.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return sorted(outputs)


def check_generated(root: Path) -> list[str]:
    outputs = generated_files(root)
    stale = []
    for rel, expected in outputs.items():
        path = root / rel
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale.append(rel)
    expected_paths = {root / rel for rel in outputs}
    for folder in (root / "views", root / "generated"):
        if folder.exists():
            for path in folder.rglob("*"):
                if path.is_file() and path not in expected_paths:
                    stale.append(path.relative_to(root).as_posix())
    return sorted(set(stale))


def validate(root: Path, *, check_views: bool = True) -> dict[str, Any]:
    root = root.resolve()
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    def add(code: str, path: str | Path, detail: str, warning: bool = False) -> None:
        rel = path.relative_to(root).as_posix() if isinstance(path, Path) and path.is_absolute() else str(path)
        (warnings if warning else errors).append({"code": code, "file": rel, "detail": detail})

    try:
        publication = json.loads((root / "publication.json").read_text(encoding="utf-8"))
    except Exception as exc:
        publication = {}
        add("publication", "publication.json", f"invalid or missing: {exc}")
    if publication.get("kps_language") != "12.x": add("language", "publication.json", "expected KPS 12.x")
    if publication.get("vocabulary_policy") != "open-authored-kebab-case": add("vocabulary", "publication.json", "unexpected vocabulary policy")

    for forbidden in FORBIDDEN_DIRS:
        if (root / forbidden).exists(): add("forbidden-folder", forbidden, "active architecture forbids this folder")
    for folder in [*ROLE_FOLDERS.values(), "sources", "sequences", "tools", "tests"]:
        if not (root / folder).is_dir(): add("folder", folder, "missing required folder")

    docs: list[Document] = []
    for folder in [*ROLE_FOLDERS.values(), "sources", "sequences"]:
        for path in sorted((root / folder).glob("*.md")):
            try: docs.append(parse_document(path, root))
            except Exception as exc: add("parse", path, str(exc))

    by_id: dict[str, Document] = {}
    aliases: dict[str, str] = {}
    for doc in docs:
        meta = doc.meta
        ident = meta.get("id")
        if not isinstance(ident, str) or not ID_RE.fullmatch(ident):
            add("id", doc.path, f"invalid id {ident!r}")
            continue
        if ident in by_id or ident in aliases: add("duplicate-id", doc.path, ident)
        by_id[ident] = doc
        for alias in meta.get("aliases", []) if isinstance(meta.get("aliases", []), list) else []:
            if not isinstance(alias, str) or not ID_RE.fullmatch(alias): add("alias", doc.path, f"invalid alias {alias!r}")
            elif alias in by_id or alias in aliases: add("duplicate-alias", doc.path, alias)
            else: aliases[alias] = ident

    all_ids = set(by_id) | set(aliases)
    knowledge = [d for d in docs if d.role]
    sources = [d for d in docs if d.kind == "source"]
    sequences = [d for d in docs if d.kind == "sequence"]

    for doc in docs:
        meta = doc.meta
        required = ["id", "version", "language", "status"]
        for key in required:
            if key not in meta: add("metadata", doc.path, f"missing {key}")
        if meta.get("language") != "KPS 12.x": add("language", doc.path, "expected KPS 12.x")
        if "type" in meta or "role" in meta or "roles" in meta: add("redundant-role", doc.path, "folder determines the primary role")
        if sum(1 for level, _ in doc.headings if level == 1) != 1: add("title", doc.path, "exactly one H1 required")
        if not doc.section("Key takeaway"): add("section", doc.path, "missing Key takeaway")
        if not doc.section("Summary"): add("section", doc.path, "missing Summary")

        if doc.role:
            for key in ["domains", "evidence_status", "source_status", "basis_kind", "reviewed", "claims", "relations", "sources"]:
                if key not in meta: add("metadata", doc.path, f"missing {key}")
            if meta.get("reviewed") is not None and meta.get("evidence_status") == "provisional": add("review", doc.path, "provisional item cannot claim reviewed date")
            if not doc.section("Evidence status"): add("section", doc.path, "missing Evidence status")
            for section in ROLE_SECTIONS[doc.role]:
                if not doc.section(section): add("role-section", doc.path, f"{doc.role} missing {section}")
            claims = meta.get("claims")
            if not isinstance(claims, list) or not claims: add("claims", doc.path, "nonempty claims list required")
            else:
                seen_claims = set()
                for claim in claims:
                    if not isinstance(claim, dict): add("claims", doc.path, "claim must be object"); continue
                    cid = claim.get("id")
                    if not isinstance(cid, str) or not PREDICATE_RE.fullmatch(cid): add("claim-id", doc.path, str(cid))
                    elif cid in seen_claims: add("claim-id", doc.path, f"duplicate {cid}")
                    seen_claims.add(cid)
                    if not claim.get("statement") or not claim.get("scope") or not claim.get("evidence_status"): add("claim", doc.path, f"incomplete claim {cid}")
                key_claim = next((c for c in claims if c.get("id") == "key-takeaway"), None)
                if not key_claim: add("claim", doc.path, "missing key-takeaway claim")
                elif key_claim.get("statement") != doc.key_takeaway: add("claim-sync", doc.path, "key-takeaway claim differs from visible section")
            domains = meta.get("domains")
            if not isinstance(domains, list) or not domains: add("domains", doc.path, "nonempty domain list required")
            else:
                for domain in domains:
                    if not isinstance(domain, str) or not TERM_RE.fullmatch(domain): add("domain", doc.path, f"invalid {domain!r}")
            relations = meta.get("relations")
            if not isinstance(relations, list): add("relations", doc.path, "relations must be list")
            else:
                for relation in relations:
                    if not isinstance(relation, dict): add("relation", doc.path, "relation must be object"); continue
                    predicate = relation.get("predicate")
                    target = relation.get("target")
                    if not isinstance(predicate, str) or not PREDICATE_RE.fullmatch(predicate): add("predicate", doc.path, f"invalid {predicate!r}")
                    if not isinstance(target, str) or target not in all_ids: add("relation-target", doc.path, f"unresolved {target!r}")
                    expected = relation.get("expected_role")
                    canonical = aliases.get(target, target) if isinstance(target, str) else None
                    target_doc = by_id.get(canonical) if canonical else None
                    if expected and (not target_doc or target_doc.role != expected): add("relation-role", doc.path, f"{target} is not {expected}")
                    claim = relation.get("claim")
                    if claim and claim not in {c.get("id") for c in meta.get("claims", [])}: add("relation-claim", doc.path, f"unknown claim {claim}")
            src_refs = meta.get("sources")
            if not isinstance(src_refs, list): add("sources", doc.path, "sources must be list")
            else:
                for source in src_refs:
                    if not isinstance(source, dict): add("source-ref", doc.path, "source entry must be object"); continue
                    sid = source.get("id")
                    canonical = aliases.get(sid, sid)
                    if canonical not in by_id or by_id[canonical].kind != "source": add("source-ref", doc.path, f"unresolved source {sid!r}")
                    if source.get("relation") not in {"context-only", "supports", "qualifies", "contradicts", "illustrates"}: add("source-relation", doc.path, f"invalid {source.get('relation')!r}")
                    if source.get("relation") != "context-only" and not source.get("claim"): add("source-claim", doc.path, "claim-level evidence requires claim id")
            if doc.meta.get("interface") is not None:
                if doc.role != "model": add("interface-role", doc.path, "only Models may declare interface")
                interface = doc.meta.get("interface")
                if not isinstance(interface, dict): add("interface", doc.path, "interface must be object")
                else:
                    for key in ["source_domain", "source_representation", "predicate", "target_domain", "target_representation", "claim", "scope", "cardinality"]:
                        if not interface.get(key): add("interface", doc.path, f"missing {key}")
                    for key in ["source_domain", "target_domain"]:
                        if interface.get(key) not in meta.get("domains", []): add("interface-domain", doc.path, f"{key} not in domains")
                    if interface.get("predicate") and not PREDICATE_RE.fullmatch(interface["predicate"]): add("interface-predicate", doc.path, interface["predicate"])
                    if interface.get("claim") not in {c.get("id") for c in meta.get("claims", [])}: add("interface-claim", doc.path, str(interface.get("claim")))
            if doc.role == "practice":
                stages = [(int(m.group(1)), m.group(2)) for m in re.finditer(r"^## Stage(\d+) (.+)$", doc.body, re.M)]
                if not stages: add("practice-stage", doc.path, "Practice needs StageN headings")
                elif [n for n, _ in stages] != list(range(1, len(stages) + 1)): add("practice-stage", doc.path, "Stage numbering must be consecutive")
                for label in ["Goal", "Why", "What to do", "What to observe", "Success signal", "Next"]:
                    if not re.search(rf"\*\*{re.escape(label)}(?::)?\*\*", doc.body): add("practice-stage", doc.path, f"missing repeated {label} labels")

        elif doc.kind == "source":
            for key in ["creator", "publication", "publication_date", "date_basis", "accessed", "access_extent", "reviewed"]:
                if key not in meta: add("source-metadata", doc.path, f"missing {key}")
            if not doc.section("Nonclaims"): add("source-section", doc.path, "missing Nonclaims")
            if not any(urlsplit(link).scheme in {"http", "https"} for link in doc.links): add("source-url", doc.path, "no external publication URL")
        elif doc.kind == "sequence":
            stages = meta.get("stages")
            if not isinstance(stages, list) or not stages: add("sequence", doc.path, "nonempty stages required")
            else:
                seen = set()
                for stage in stages:
                    if not isinstance(stage, dict) or not stage.get("id") or not stage.get("label") or not isinstance(stage.get("members"), list): add("sequence-stage", doc.path, str(stage)); continue
                    if stage["id"] in seen: add("sequence-stage", doc.path, f"duplicate {stage['id']}")
                    seen.add(stage["id"])
                    for member in stage["members"]:
                        if member not in all_ids: add("sequence-member", doc.path, f"unresolved {member}")

        # Local link validation.
        heading_slugs = {slug(h) for _, h in doc.headings}
        for link in doc.links:
            parsed = urlsplit(link)
            if parsed.scheme in {"http", "https", "mailto"}: continue
            if link.startswith("#"):
                if slug(link[1:]) not in heading_slugs: add("anchor", doc.path, f"missing local anchor {link}")
                continue
            base, _, fragment = link.partition("#")
            target = (doc.path.parent / base).resolve()
            try: target.relative_to(root)
            except ValueError: add("link", doc.path, f"escapes repository: {link}"); continue
            if not target.exists(): add("link", doc.path, f"missing target {link}")
            elif fragment and target.suffix == ".md":
                try: target_doc = parse_document(target, root) if target.parent.name in {*ROLE_FOLDERS.values(), "sources", "sequences"} else None
                except Exception: target_doc = None
                if target_doc and slug(fragment) not in {slug(h) for _, h in target_doc.headings}: add("anchor", doc.path, f"missing target anchor {link}")

    # Foundation coverage and required interfaces.
    domain_counts = Counter()
    domain_roles: dict[str, set[str]] = defaultdict(set)
    for doc in knowledge:
        for domain in doc.meta.get("domains", []):
            top = top_domain(domain)
            domain_counts[top] += 1
            domain_roles[top].add(doc.role or "")
    for domain in publication.get("foundation_domains", []):
        if domain_counts[domain] < 5: add("coverage", "publication.json", f"{domain} has only {domain_counts[domain]} knowledge items")
        if "concept" not in domain_roles[domain]: add("coverage", "publication.json", f"{domain} lacks a Concept")
        if not ({"model", "method"} & domain_roles[domain]): add("coverage", "publication.json", f"{domain} lacks Model or Method coverage")
    actual_interfaces = {(d.meta["interface"]["source_domain"], d.meta["interface"]["target_domain"]) for d in knowledge if d.meta.get("interface")}
    for pair in publication.get("required_interfaces", []):
        if tuple(pair) not in actual_interfaces: add("interface-coverage", "publication.json", f"missing {pair}")

    # Advisory possible vocabulary collisions: normalized singular-ish forms.
    vocab = sorted({domain for doc in knowledge for domain in doc.meta.get("domains", [])})
    normalized: dict[str, list[str]] = defaultdict(list)
    for term in vocab:
        normalized[term.replace("-and-", "-").replace("-structure", "")].append(term)
    for forms in normalized.values():
        if len(set(forms)) > 1: add("vocabulary-review", "generated/domains.json", ", ".join(sorted(forms)), warning=True)

    if check_views:
        for stale in check_generated(root): add("generated", stale, "missing or stale generated output")

    stats = {
        "knowledge_items": len(knowledge),
        "by_role": dict(Counter(d.role for d in knowledge)),
        "sources": len(sources),
        "sequences": len(sequences),
        "claims": sum(len(d.meta.get("claims", [])) for d in knowledge),
        "relations": sum(len(d.meta.get("relations", [])) for d in knowledge),
        "interfaces": sum(1 for d in knowledge if d.meta.get("interface")),
        "domains": len({x for d in knowledge for x in d.meta.get("domains", [])}),
    }
    return {"ok": not errors, "scope": "structural coherence, coverage declarations and generated-view freshness; not factual certification", "stats": stats, "errors": errors, "warnings": warnings}
