from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/orders")
def orders():
    return jsonify(message="Orders service running")

app.run(host="0.0.0.0", port=5000)