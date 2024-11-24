from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Get the Make.com webhook URL from environment variables
MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

@app.route("/vat-report", methods=["POST"])
def fetch_vat_report():
    # Example to confirm the endpoint works
    data = request.json
    return jsonify({"message": "Endpoint works!", "received": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
