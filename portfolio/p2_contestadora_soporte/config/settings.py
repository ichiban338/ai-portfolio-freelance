# config/settings.py – Contestadora AI TechSolve
import os

ANTHROPIC_API_KEY  = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL       = "claude-opus-4-6"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE       = os.environ.get("TWILIO_PHONE", "")
HOST, PORT, DEBUG  = "0.0.0.0", 5001, False
