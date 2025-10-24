# AegisLab Report (Synthetic)

**Generated:** 2025-10-23T22:23:26.767152

## Summary

- Source log: `http_1761276206.log`
- Status code counts: `{'200': 248, '401': 52}`
- Anomaly: Excessive failed logins from IP(s): 192.168.1.22, 127.0.0.1

## Top Paths

- /product/7: 71
- /: 68
- /product/1: 57
- /search?q=gift: 52
- /login: 52

## ATT&CK-ish Mapping (Illustrative)

- Excessive failed logins → Credential Access
- Path enumeration → Discovery