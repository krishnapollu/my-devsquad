#!/usr/bin/env python3
"""Small, local DevSquad helper; uses only the Python standard library."""
from pathlib import Path
import argparse, json, subprocess, sys

STATE_DIR = Path(".devsquad")
STATE = STATE_DIR / "state.json"
TEMPLATES = Path(__file__).parent / "templates"

def git(*args):
    try:
        return subprocess.run(["git", *args], text=True, capture_output=True, check=False).stdout.strip()
    except OSError:
        return "git unavailable"

def init():
    STATE_DIR.mkdir(exist_ok=True)
    if not STATE.exists():
        data = json.loads((TEMPLATES / "state.json").read_text())
        data["branch"] = git("branch", "--show-current")
        data["working_tree"] = "clean" if not git("status", "--porcelain") else "dirty"
        STATE.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Initialized {STATE}")

def status():
    if not STATE.exists():
        print("No checkpoint found. Run: python3 devsquad.py init")
        return 1
    print(STATE.read_text(), end="")
    print("\nCurrent git:")
    print(f"branch: {git('branch', '--show-current')}")
    print(f"working tree: {'clean' if not git('status', '--porcelain') else 'dirty'}")
    return 0

def validate():
    result = subprocess.run([sys.executable, "scripts/validate.py"], text=True)
    return result.returncode

parser = argparse.ArgumentParser(description="Local DevSquad checkpoint helper")
parser.add_argument("command", choices=["init", "status", "inspect", "validate"])
args = parser.parse_args()

def inspect():
    return subprocess.run([sys.executable, "scripts/inspect.py"], check=False).returncode

sys.exit({"init": init, "status": status, "inspect": inspect, "validate": validate}[args.command]())
