#!/usr/bin/env python3
"""Dependency-free structural validation for the DevSquad plugin."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(path):
    p = ROOT / path
    if not p.exists(): errors.append(f"missing {path}")
    return p

for manifest in ("plugin.json", ".codex-plugin/plugin.json"):
    p = require(manifest)
    if p.exists():
        try: json.loads(p.read_text())
        except Exception as exc: errors.append(f"invalid JSON {manifest}: {exc}")

skills = list((ROOT / "skills").glob("*/SKILL.md"))
if len(skills) < 6: errors.append(f"expected at least 6 skills, found {len(skills)}")
for p in skills:
    text = p.read_text()
    if not text.startswith("---\n") or "name:" not in text or "description:" not in text:
        errors.append(f"missing skill frontmatter in {p.relative_to(ROOT)}")

for template in ("templates/spec.md", "templates/state.md", "templates/decisions.md"):
    require(template)

for doc in ("README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"):
    require(doc)

if errors:
    print("Validation failed:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Validation passed: {len(skills)} skills, manifests, templates, and project docs present.")
