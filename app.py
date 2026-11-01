import os
import socket
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "1.0")


@app.route("/")
def home():
    # hostname = the Pod name inside Kubernetes -> shows load balancing across replicas
    return f"""
    <html><body style="font-family:sans-serif;text-align:center;margin-top:80px">
      <h1>Hello from Docker + Kubernetes!</h1>
      <p>Served by pod: <b>{socket.gethostname()}</b></p>
      <p>App version: {VERSION}</p>
      <p>Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </body></html>
    """


@app.route("/health")
def health():
    # Used by Kubernetes liveness/readiness probes
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
