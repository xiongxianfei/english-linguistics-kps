#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from kpslib import build_state, top_domain

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    parser = argparse.ArgumentParser(description="Query the canonical KPS 12 Markdown graph.")
    parser.add_argument("--id")
    parser.add_argument("--domain")
    parser.add_argument("--relation")
    parser.add_argument("--interfaces", action="store_true")
    args = parser.parse_args()
    state = build_state(ROOT)
    if args.id:
        ident = state["aliases"].get(args.id, args.id)
        doc = state["by_id"].get(ident)
        if not doc:
            print(f"Unknown ID: {args.id}")
            return 1
        print(json.dumps({"id": ident, "title": doc.title, "role": doc.role, "path": doc.relpath, "domains": doc.meta.get("domains", []), "relations": doc.meta.get("relations", []), "claims": doc.meta.get("claims", [])}, ensure_ascii=False, indent=2))
        return 0
    if args.domain:
        rows = []
        for doc in state["knowledge"]:
            if any(d == args.domain or d.startswith(args.domain + ":") or top_domain(d) == args.domain for d in doc.meta.get("domains", [])):
                rows.append((doc.title, doc.role, doc.relpath))
        for title, role, path in sorted(rows): print(f"{role:9} {title} — {path}")
        return 0 if rows else 1
    if args.relation:
        rows = state["relation_uses"].get(args.relation, [])
        for row in rows: print(f"{row['source']} --{args.relation}--> {row['target']} [{row.get('layer','semantic')}]")
        return 0 if rows else 1
    if args.interfaces:
        for item in state["interfaces"]:
            print(f"{item['id']}: {item['source_domain']}/{item['source_representation']} --{item['predicate']}--> {item['target_domain']}/{item['target_representation']}")
        return 0
    parser.print_help()
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
