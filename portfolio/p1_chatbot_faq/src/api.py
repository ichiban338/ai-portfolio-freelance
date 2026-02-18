# ============================================================
# src/api.py – Servidor Flask para el chatbot
# ============================================================

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, request, jsonify
from chatbot_engine import ChatBotEngine
from config.settings import HOST, PORT, DEBUG, ANTHROPIC_API_KEY

app = Flask(__name__)
bot = ChatBotEngine(api_key=ANTHROPIC_API_KEY)

# ----------------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data       = request.get_json(silent=True) or {}
    session_id = data.get("session_id", "anon")
    message    = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Mensaje vacío"}), 400
    result = bot.chat(session_id, message)
    return jsonify(result)

@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify(bot.get_metrics())

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "bot": "Sofia – TrendStore FAQ"})

# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
