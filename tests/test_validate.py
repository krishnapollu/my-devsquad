import subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DevSquadTests(unittest.TestCase):
  def test_plugin_structure(self):
    result = subprocess.run([sys.executable, ROOT / "scripts/validate.py"], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

  def test_local_helper_help(self):
    result = subprocess.run([sys.executable, ROOT / "devsquad.py", "--help"], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0)

  def test_inspection_helper(self):
    result = subprocess.run([sys.executable, ROOT / "devsquad.py", "inspect"], capture_output=True, text=True)
    self.assertEqual(result.returncode, 0)
    self.assertIn("Working tree:", result.stdout)
