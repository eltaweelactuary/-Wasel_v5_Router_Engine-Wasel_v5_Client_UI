import os
import requests
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ── Konecta SaaS Engine Config ──
# This isolates and protects your cloud infrastructure URL from the frontend UI
SAAS_URL = "https://wasel-v5-router-112458895076.europe-west1.run.app"

@app.route('/')
def index():
    """Serve the pristine, logicless frontend UI to the partner."""
    with open("index.html", "r", encoding="utf-8") as f:
        return render_template_string(f.read())

@app.route('/t', methods=['POST'])
def proxy_translate():
    """Secure Proxy: Forwards coordinates to SaaS Engine."""
    try:
        data = request.json
        response = requests.post(f"{SAAS_URL}/t", json=data, timeout=10)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print(f"Proxy Error: {e}")
        return jsonify({"translation": "Err: Proxy Connection Failed", "source": "proxy-error"}), 500

@app.route('/chat', methods=['POST'])
def proxy_chat():
    """Secure Proxy: Forwards text to SaaS Chat Engine."""
    try:
        data = request.json
        response = requests.post(f"{SAAS_URL}/chat", json=data, timeout=10)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print(f"Proxy Error: {e}")
        return jsonify({"reply": "حدث خطأ في الاتصال بالخادم. يرجى المحاولة لاحقاً."}), 500

if __name__ == '__main__':
    print("==================================================")
    print("🚀 WASEL V5 PARTNER CLIENT PROXY STARTED")
    print(f"🔗 Target SaaS Backend : {SAAS_URL}")
    print("🌐 UI Accessible at    : http://localhost:5000")
    print("==================================================")
    app.run(host='0.0.0.0', port=5000)
