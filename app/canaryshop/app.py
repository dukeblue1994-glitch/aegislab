
from flask import Flask, request, jsonify
import os, logging

app = Flask(__name__)
log_path = os.environ.get("LOG_PATH", "/tmp/canaryshop.log")
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s %(message)s")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/login")
def login():
    user = request.json.get("user","unknown") if request.is_json else "unknown"
    logging.info(f'login_attempt user="{user}" ip="{request.remote_addr}" ua="{request.headers.get("User-Agent","")}" result=fail')
    return jsonify({"ok": False, "reason": "demo"}), 401

@app.get("/search")
def search():
    q = request.args.get("q","")
    logging.info(f'search query="{q}" ip="{request.remote_addr}"')
    return jsonify({"results": [], "q": q})

@app.get("/product/<pid>")
def product(pid):
    logging.info(f'product_view id="{pid}" ip="{request.remote_addr}"')
    return jsonify({"id": pid, "name": f"Item {pid}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
