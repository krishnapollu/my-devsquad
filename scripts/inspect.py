#!/usr/bin/env python3
"""Print a compact, deterministic repository briefing without third-party packages."""
from pathlib import Path
import json, subprocess

ROOT = Path.cwd()
markers = {
    "Python": ["pyproject.toml", "requirements.txt", "setup.py"],
    "JavaScript/TypeScript": ["package.json", "tsconfig.json"],
    "Go": ["go.mod"],
    "Rust": ["Cargo.toml"],
    ".NET": ["*.csproj", "*.sln"],
    "Java/Kotlin": ["pom.xml", "build.gradle", "build.gradle.kts"],
}

def git(*args):
    result = subprocess.run(["git", *args], text=True, capture_output=True, check=False)
    return result.stdout.strip() or result.stderr.strip()

print(f"Repository: {ROOT}")
print(f"Branch: {git('branch', '--show-current')}")
print(f"Working tree: {'clean' if not git('status', '--porcelain') else 'dirty'}")
print("Detected ecosystems:")
found = False
for name, paths in markers.items():
    hits = [p for pattern in paths for p in ROOT.glob(pattern)]
    if hits:
        found = True
        print(f"- {name}: {', '.join(sorted({str(p.relative_to(ROOT)) for p in hits}))}")
if not found:
    print("- none detected")

print("Instructions:")
for name in ("AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md", "CONTRIBUTING.md"):
    if (ROOT / name).exists(): print(f"- {name}")

for name in ("package.json", "pyproject.toml"):
    p = ROOT / name
    if p.exists() and p.suffix == ".json":
        try:
            data = json.loads(p.read_text())
            scripts = data.get("scripts", {})
            if scripts: print(f"Scripts ({name}): {', '.join(sorted(scripts))}")
        except (OSError, json.JSONDecodeError):
            print(f"Scripts ({name}): unreadable")
