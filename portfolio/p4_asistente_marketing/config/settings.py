# config/settings.py – Asistente AI DigitalPulse
import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL      = "claude-opus-4-6"
OUTPUT_DIR        = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
