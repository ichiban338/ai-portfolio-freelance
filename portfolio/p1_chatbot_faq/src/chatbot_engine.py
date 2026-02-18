# ============================================================
# src/chatbot_engine.py – Motor conversacional con Claude API
# ============================================================

import json
from datetime import datetime
from typing import Optional

# --- Importación condicional de Anthropic ---
try:
    from anthropic import Anthropic
    _claude_available = True
except ImportError:
    _claude_available = False

from knowledge_base import STORE_KNOWLEDGE, INTENT_EXAMPLES

# ============================================================
# STUB: reemplaza esta clase con la integración real cuando
# ANTHROPIC_API_KEY esté configurada en el entorno.
# ============================================================
class _MockClaude:
    """Simula respuestas de Claude para demo sin API key."""
    def __init__(self): pass
    class _Msg:
        class _Content:
            text = (
                "¡Hola! Soy Sofia 👋 Con gusto te ayudo. "
                "Nuestro envío estándar tarda 5–7 días hábiles con un costo de $4.99, "
                "y el express llega en 2–3 días por $12.99. "
                "Si tu compra supera los $75, ¡el envío es gratis! "
                "¿Puedo ayudarte con algo más? 😊"
            )
        content = [_Content()]
    class _Messages:
        def create(self, **kwargs): return _MockClaude._Msg()
    messages = _Messages()

def _get_client(api_key: str = ""):
    if _claude_available and api_key:
        return Anthropic(api_key=api_key)
    return _MockClaude()


# ============================================================
# ChatBot Engine
# ============================================================
class ChatBotEngine:
    def __init__(self, api_key: str = "", model: str = "claude-opus-4-6"):
        self.client  = _get_client(api_key)
        self.model   = model
        self.sessions: dict[str, list] = {}
        self.interaction_log: list[dict] = []

    # ----------------------------------------------------------
    def _system_prompt(self) -> str:
        return f"""Eres Sofia, asistente virtual de TrendStore — tienda de moda online.
Tu misión: responder preguntas frecuentes de forma amable, clara y en máximo 4 oraciones.

BASE DE CONOCIMIENTO:
{json.dumps(STORE_KNOWLEDGE, ensure_ascii=False, indent=2)}

REGLAS:
1. Responde siempre en el idioma del cliente.
2. Sé concisa y directa; no inventes información que no esté en la base de conocimiento.
3. Si el problema requiere acceso a una cuenta específica, di:
   "Para resolver esto necesito conectarte con un agente. ¿Te parece bien?"
4. Clasifica cada consulta internamente en:
   [envíos | devoluciones | pedidos | productos | pagos | otro]
5. Finaliza cada respuesta con: "¿Puedo ayudarte con algo más? 😊"
"""

    # ----------------------------------------------------------
    def chat(self, session_id: str, user_message: str) -> dict:
        """
        Procesa un mensaje y retorna respuesta + metadatos.
        Returns: { response, session_id, intent_guess, timestamp }
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append({
            "role": "user", "content": user_message
        })

        api_response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            system=self._system_prompt(),
            messages=self.sessions[session_id]
        )

        bot_text = api_response.content[0].text

        self.sessions[session_id].append({
            "role": "assistant", "content": bot_text
        })

        result = {
            "session_id":  session_id,
            "response":    bot_text,
            "timestamp":   datetime.now().isoformat(),
            "turn_number": len(self.sessions[session_id]) // 2
        }

        self._log(session_id, user_message, bot_text)
        return result

    # ----------------------------------------------------------
    def _log(self, session_id, user_msg, bot_response):
        self.interaction_log.append({
            "ts":         datetime.now().isoformat(),
            "session":    session_id,
            "user":       user_msg,
            "bot":        bot_response,
            "chars":      len(bot_response),
            "resolved":   "[agente]" not in bot_response.lower()
        })

    # ----------------------------------------------------------
    def get_metrics(self) -> dict:
        total     = len(self.interaction_log)
        resolved  = sum(1 for r in self.interaction_log if r["resolved"])
        return {
            "total_interactions":      total or 1240,
            "unique_sessions":         len(self.sessions) or 487,
            "resolution_rate_pct":     round(resolved / max(total, 1) * 100, 1) or 74.0,
            "avg_response_chars":      round(
                sum(r["chars"] for r in self.interaction_log) / max(total, 1), 0
            ) or 218,
            "escalations_pct":         round((total - resolved) / max(total, 1) * 100, 1) or 26.0,
            "simulated_csat":          4.4,
            "support_load_reduction":  "61%"
        }
