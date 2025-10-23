
import pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_emulation_runs():
    rc = subprocess.call([sys.executable, str(ROOT/"emulation"/"synth_attack_emulator.py")])
    assert rc == 0

def test_analyze_then_report():
    rc = subprocess.call([sys.executable, str(ROOT/"tools"/"aegisctl.py"), "analyze"])
    assert rc in (0, None)
    rc = subprocess.call([sys.executable, str(ROOT/"tools"/"aegisctl.py"), "report"])
    assert rc in (0, None)
