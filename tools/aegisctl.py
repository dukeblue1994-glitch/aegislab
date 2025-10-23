
#!/usr/bin/env python3
import argparse, pathlib, re, yaml, sys, datetime as dt
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic"
REPORT = ROOT / "report" / "aegislab-report.md"
SIGMA_DIR = ROOT / "detections" / "sigma"

def synth():
    import subprocess, sys
    emu = ROOT / "emulation" / "synth_attack_emulator.py"
    return subprocess.call([sys.executable, str(emu)])

def analyze():
    logs = sorted(DATA.glob("*.log"))
    if not logs:
        print("No synthetic logs found. Run: aegisctl.py synth")
        return 1
    latest = logs[-1]
    code_re = re.compile(r'"\s(\d{3})\s')
    path_re = re.compile(r'"\w+\s([^\s]+)\sHTTP')
    ip_re = re.compile(r'^(\S+)\s')
    codes=Counter(); paths=Counter(); ips=Counter(); logins=Counter()
    with latest.open() as f:
        for ln in f:
            c = code_re.search(ln); p = path_re.search(ln); ipm = ip_re.search(ln)
            if c: codes[c.group(1)]+=1
            if p: paths[p.group(1)]+=1
            if ipm: ips[ipm.group(1)]+=1
            if "/login" in ln and " 401 " in ln and ipm: logins[ipm.group(1)]+=1
    print("Latest log:", latest.name)
    print("HTTP status counts:", dict(codes))
    print("Top paths:", paths.most_common(5))
    if any(v>10 for v in logins.values()):
        print("Anomaly: excessive 401s per IP (synthetic brute-force pattern).")
    findings = ROOT / "report" / "findings.yaml"
    findings.write_text(yaml.safe_dump({
        "generated": dt.datetime.now().isoformat(),
        "log": latest.name,
        "codes": dict(codes),
        "top_paths": paths.most_common(5),
        "excessive_401_ips": [ip for ip,v in logins.items() if v>10]
    }))
    print("Wrote findings to", findings)
    return 0

def report():
    findings = ROOT / "report" / "findings.yaml"
    if not findings.exists():
        print("No findings.yaml. Run analyze first.")
        return 1
    data = yaml.safe_load(findings.read_text())
    md = []
    md.append("# AegisLab Report (Synthetic)\n")
    md.append(f"**Generated:** {dt.datetime.now().isoformat()}\n")
    md.append("## Summary\n")
    md.append(f"- Source log: `{data['log']}`")
    md.append(f"- Status code counts: `{data['codes']}`")
    if data['excessive_401_ips']:
        md.append(f"- Anomaly: Excessive failed logins from IP(s): {', '.join(data['excessive_401_ips'])}")
    md.append("\n## Top Paths\n")
    for p,c in data["top_paths"]:
        md.append(f"- {p}: {c}")
    md.append("\n## ATT&CK-ish Mapping (Illustrative)\n")
    md.append("- Excessive failed logins → Credential Access")
    md.append("- Path enumeration → Discovery")
    REPORT.write_text("\n".join(md))
    print("Wrote report:", REPORT)
    return 0

def validate_sigma():
    ok=True
    for y in SIGMA_DIR.glob("*.yml"):
        try:
            yaml.safe_load(y.read_text())
            print("OK:", y.name)
        except Exception as e:
            print("Invalid YAML:", y, e)
            ok=False
    return 0 if ok else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["synth","analyze","report","validate-sigma"])
    args = ap.parse_args()
    return globals()[args.cmd]()

if __name__ == "__main__":
    sys.exit(main())
