# ============================================================
# PROYECTO 1 – Chatbot FAQ Inteligente
# config/settings.py – Configuración centralizada
# ============================================================

import os

# --- API (set via .env en producción) ---
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL       = "claude-opus-4-6"
MAX_TOKENS         = 512

# --- Servidor ---
HOST = "0.0.0.0"
PORT = 5000
DEBUG = False

# --- Bot ---
BOT_NAME    = "Sofia"
STORE_NAME  = "TrendStore"
LANGUAGE    = "es"

# --- Paths ---
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR  = os.path.join(BASE_DIR, "outputs")
DOCS_DIR    = os.path.join(BASE_DIR, "docs")
