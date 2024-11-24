from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Get the Make.com webhook URL from environment variables
MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

@app.route("/vat-report", methods=["POST"])
def fetch_vat_report():
    data = request.json
    try:
        # Forward the request to the Make.com webhook
        response = requests.post(MAKE_WEBHOOK_URL, json=data)
        
        # Debug logging
        print(f"Make.com Response Status Code: {response.status_code}")
        print(f"Make.com Response Body: {response.text}")
        
        # Ensure the response from Make.com is JSON
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        # Log the error and return a 500 response with details
        print(f"Error: {e}")
        return jsonify({"error": "Failed to process request", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
