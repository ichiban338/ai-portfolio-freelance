# config/settings.py – ContactPro Call Center AI
import os

ANTHROPIC_API_KEY  = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL       = "claude-opus-4-6"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "")
N_CALLS_SIMULATE   = 500
OUTPUT_DIR         = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
