import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_plugin_structure():
    result = subprocess.run([sys.executable, ROOT / "scripts/validate.py"], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
