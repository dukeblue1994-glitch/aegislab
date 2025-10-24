# AegisLab Report (Synthetic)

**Generated:** 2025-10-23T22:23:09.252886

## Summary

- Source log: `http_1761276181.log`
- Status code counts: `{'200': 253, '401': 47}`
- Anomaly: Excessive failed logins from IP(s): 10.0.0.6, 192.168.1.22

## Top Paths

- /: 70
- /product/1: 68
- /product/7: 61
- /search?q=gift: 54
- /login: 47

## ATT&CK-ish Mapping (Illustrative)

- Excessive failed logins → Credential Access
- Path enumeration → Discovery