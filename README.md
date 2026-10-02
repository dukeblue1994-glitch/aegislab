# AegisLab

**A local lab for synthetic security events, detection analytics, and reproducible reports.**

[![CI](https://github.com/dukeblue1994-glitch/aegislab/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dukeblue1994-glitch/aegislab/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](tools/requirements.txt)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Built by [Nick Anderson](https://github.com/dukeblue1994-glitch). AegisLab generates synthetic web application logs, analyzes activity patterns, and produces a report from the resulting evidence. It is a portfolio and learning environment for detection engineering.

```text
GENERATE              ANALYZE                 EXPLAIN
Synthetic logs  -->  Rules + anomalies  -->  Findings + report
```

## Explore the project

| Area | What it contains |
| --- | --- |
| [Emulation](emulation/) | Synthetic security event generation |
| [Detection rules](detections/) | Sigma-style rule definitions |
| [Analysis](analysis/) | Notebooks and analytical exploration |
| [Tools](tools/) | CLI commands, analytics, and report generation |
| [Reports](report/) | Findings and generated report artifacts |
| [Infrastructure](infra/) | Optional local Docker environment |

## Run the local workflow

Requires Python 3.11 or newer. From the repository root:

```bash
python -m venv .venv
# Activate .venv for your shell, then:
python -m pip install -r tools/requirements.txt
python tools/aegisctl.py synth
python tools/aegisctl.py analyze
python tools/aegisctl.py report
```

Read the generated report at `report/aegislab-report.md`. To explore the additional analytics demonstration:

```bash
python tools/aegisctl.py demo-advanced
```

You can also inspect `analysis/advanced_threat_hunting.ipynb`. For the optional local application environment:

```bash
docker compose -f infra/docker-compose.yml up
```

## Scope

The lab uses synthetic events for local analysis. Report mappings are illustrative and should be assessed in that context. Keep the environment bound to localhost and use only systems you own or have explicit authorization to test.

See [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and the [MIT license](LICENSE).
