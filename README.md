# AegisLab — Synthetic Offensive Emulation & Detection (Local • Safe)

![CI](https://github.com/dukeblue1994-glitch/aegislabs/actions/workflows/ci.yml/badge.svg?branch=main)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

*Built by **Nick Anderson**. This repo spins up a tiny instrumented app, generates **synthetic security events**, runs detection analytics, and auto-produces an executive-style report—no exploits, entirely local, and legally safe.*

# AegisLab — Offensive Emulation & Detection Portfolio (Legal, Lab-Only)

**Author:** Nick Anderson  
**Purpose:** Demonstrate end-to-end red-team *emulation* and blue-team *detection* skills—legally—using a self-contained lab.
This project spins up a tiny instrumented demo app, generates **synthetic security-relevant logs** (no exploits),
runs detection analytics, and produces an executive-style report automatically.

> No exploit code. No unauthorized access. Everything is local and safe.

## What it shows (at a glance)
- **Advanced Machine Learning**: Sophisticated threat hunting with Isolation Forest, DBSCAN clustering, and statistical anomaly detection
- **DevSecOps Pipeline**: Comprehensive CI/CD with security scanning, linting, and automated testing
- Reproducible infra-as-code lab (`docker-compose`) with an instrumented demo app.
- Safe **attack emulation** via synthetic event generator (failed logins, suspicious paths, noisy scans).
- Detection **rules** (Sigma-style) + **interactive Jupyter notebooks** for advanced analytics.
- Automated **report builder** that compiles findings + ATT&CK mapping from run artifacts.
- **Security-first CI** that validates Sigma rules, scans for vulnerabilities, and enforces code quality.

## Quickstart (lab-safe)
1. Ensure Python 3.11 is installed (Docker optional).
2. `pip install -r tools/requirements.txt` — install dependencies including advanced ML libraries.
3. `python3 tools/aegisctl.py synth` — generate synthetic logs into `data/synthetic/`.
4. `python3 tools/aegisctl.py analyze` — run lightweight analytics to summarize anomalies.
5. `python3 tools/aegisctl.py demo-advanced` — demonstrate advanced ML-based threat hunting.
6. `python3 tools/aegisctl.py report` — build `/report/aegislab-report.md` from artifacts.
7. (Optional) `jupyter notebook analysis/advanced_threat_hunting.ipynb` — interactive ML analysis.
8. (Optional) `docker compose -f infra/docker-compose.yml up` to run the demo app + dashboards locally.
   - **Note:** Everything binds to `127.0.0.1` and is for single-machine lab use only.

## Tech highlights
- **Advanced Analytics**: Machine Learning (scikit-learn), Statistical Analysis (scipy), Interactive Notebooks (Jupyter), Data Visualization (Plotly)
- **DevSecOps**: Multi-stage CI/CD with security scanning (Bandit, Safety, Trivy), code quality enforcement, and automated testing
- **Security**: Sigma rule validation, vulnerability scanning, compliance checking, ethical use documentation
- Python 3.11, Docker Compose, OpenSearch (optional), MITRE ATT&CK integration, comprehensive test suite.
- MIT Licensed. Clear Code of Conduct, Security Policy, and Contributing Guidelines included.

## Ethics & Scope
This repo is for **legal training**. All traffic is synthetic. Do not point any component at systems you do not own or manage with written permission.
