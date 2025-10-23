
#!/usr/bin/env python3
# Synthetic event generator (safe). Writes local-only HTTP log lines.
import pathlib, random, time, datetime as dt

out = pathlib.Path(__file__).resolve().parents[1] / "data" / "synthetic" / f"http_{int(time.time())}.log"
out.parent.mkdir(parents=True, exist_ok=True)

ips = ["127.0.0.1", "10.0.0.5", "10.0.0.6", "192.168.1.22"]
paths = ["/", "/search?q=gift", "/product/1", "/product/7", "/login"]
uas = ["AegisLabBot/1.0", "curl/8.0.1", "BrowserXYZ"]

def line(ip, method, path, code, size, ua):
    now = dt.datetime.now().strftime("%d/%b/%Y:%H:%M:%S -0500")
    return f'{ip} - - [{now}] "{method} {path} HTTP/1.1" {code} {size} "-" "{ua}"\n'

with out.open("w") as f:
    for i in range(300):
        ip = random.choice(ips)
        ua = random.choice(uas)
        if random.random() < 0.15:
            # burst of failed logins to simulate credential noise (synthetic)
            f.write(line(ip, "POST", "/login", 401, 123, ua))
        else:
            p = random.choice(paths[:-1])
            f.write(line(ip, "GET", p, 200, random.randint(256, 4096), ua))

print(f"Wrote synthetic log: {out}")
