from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICES = {
    "orders": "http://orders:5000/orders",
    "inventory": "http://inventory:5000/inventory",
    "payments": "http://payments:5000/payments"
}

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/<service>")
def gateway(service):
    if service not in SERVICES:
        return jsonify(error="Service not found"), 404

    response = requests.get(SERVICES[service])
    return jsonify(response.json())

app.run(host="0.0.0.0", port=8080)