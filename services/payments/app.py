from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/payments")
def payments():
    return jsonify(service="payments", message="Payments service running")

app.run(host="0.0.0.0", port=5000)
