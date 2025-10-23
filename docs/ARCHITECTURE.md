
# Architecture Overview

- **canaryshop**: minimal demo web app that logs user actions locally.
- **emulation**: generates synthetic events (failed logins, path hits).
- **detections**: Sigma-like rules describing what to alert on.
- **analysis**: CLI that parses logs and summarizes anomalies.
- **report**: automatic Markdown report synthesizing run artifacts.
- **infra**: optional containers for dashboards (OpenSearch + Dashboards).
