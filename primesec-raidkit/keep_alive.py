from flask import Flask, jsonify
from threading import Thread
import time

app = Flask(__name__)
start_time = time.time()


@app.route("/")
def home():
    uptime = int(time.time() - start_time)
    days = uptime // 86400
    hours = (uptime % 86400) // 3600
    minutes = (uptime % 3600) // 60

    return jsonify({
        "status": "ONLINE",
        "bot": "PRIME RAIDER",
        "uptime": f"{days}d {hours}h {minutes}m",
        "message": "PRIME RAIDER IS RUNNING"
    })


@app.route("/health")
def health():
    return "OK", 200


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
    print("[SYS] KEEP-ALIVE SERVER RUNNING ON PORT 8080")