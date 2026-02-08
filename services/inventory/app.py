from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/inventory")
def inventory():
    return jsonify(service="inventory", message="Inventory service running")

app.run(host="0.0.0.0", port=5000)
