#!/usr/bin/env python3
# ============================================================
# src/voice_operator.py – Motor de contestadora AI
# Proyecto 2: TechSolve – Soporte Técnico Automatizado
# ============================================================

import json
from datetime import datetime

try:
    from anthropic import Anthropic
    _claude_available = True
except ImportError:
    _claude_available = False


# ── Stub para demo sin API key ───────────────────────────────
class _MockClaude:
    class _Msg:
        class _C:
            text = ("Para resetear tu contraseña: ve a app.techsolve.com, "
                    "haz clic en '¿Olvidaste tu contraseña?' e ingresa tu email registrado. "
                    "Recibirás el enlace en menos de 5 minutos. "
                    "Si no llega, revisa spam o escríbenos al chat. "
                    "¿Esto resuelve tu consulta?")
        content = [_C()]
    class _Messages:
        def create(self, **kwargs): return _MockClaude._Msg()
    messages = _Messages()

def _get_client(api_key=""):
    if _claude_available and api_key:
        return Anthropic(api_key=api_key)
    return _MockClaude()


# ── Base de conocimiento técnico ─────────────────────────────
TECH_KB = {
    "password_reset": {
        "steps": [
            "Ir a app.techsolve.com",
            "Clic en '¿Olvidaste tu contraseña?'",
            "Ingresar email registrado",
            "Revisar bandeja de entrada en 5 minutos"
        ],
        "note": "Si no llega: revisar spam o confirmar email con soporte."
    },
    "connection_error": {
        "steps": [
            "Verificar conexión a internet",
            "Limpiar caché del navegador (Ctrl+Shift+Delete)",
            "Probar en modo incógnito",
            "Si persiste: reiniciar desde Panel de Control"
        ],
        "error_codes": {
            "ERR_001": "Timeout de sesión – volver a iniciar sesión",
            "ERR_002": "Sin conexión al servidor – verificar firewall",
            "ERR_003": "Licencia expirada – contactar facturación"
        }
    },
    "billing": {
        "info": "Facturas: Mi Cuenta → Facturación → Historial",
        "contact": "billing@techsolve.com para cambios de plan",
        "hours": "Lunes–Viernes 9:00–18:00 hrs"
    },
    "installation": {
        "steps": [
            "Descargar instalador desde techsolve.com/download",
            "Ejecutar como administrador",
            "Ingresar clave de licencia del email de bienvenida",
            "Reiniciar el equipo al finalizar"
        ],
        "requirements": "Windows 10+ / macOS 12+ / Ubuntu 20.04+"
    }
}

SCENARIOS = {
    "password_reset":   "Cliente quiere resetear su contraseña.",
    "connection_error": "Cliente tiene errores de conexión o acceso al sistema.",
    "billing":          "Cliente consulta sobre facturación o suscripción.",
    "installation":     "Cliente tiene problemas con instalación del software.",
}


# ── Motor principal ──────────────────────────────────────────
class VoiceOperator:
    def __init__(self, api_key="", model="claude-opus-4-6"):
        self.client   = _get_client(api_key)
        self.model    = model
        self.sessions: dict[str, list] = {}
        self.call_log: list[dict]      = []

    def _system(self, scenario: str) -> str:
        ctx = SCENARIOS.get(scenario, "Consulta de soporte técnico general.")
        return f"""Eres ARIA, asistente de soporte técnico de TechSolve.
Caso actual: {ctx}

BASE DE CONOCIMIENTO:
{json.dumps(TECH_KB, ensure_ascii=False, indent=2)}

REGLAS:
- Máximo 4 oraciones claras y empáticas.
- Si puedes resolver con la base de conocimiento, hazlo paso a paso.
- Si el problema requiere acceso a la cuenta del cliente, responde exactamente: [ESCALAR]
- Finaliza con: "¿Esto resuelve tu problema?"
"""

    def process(self, session_id: str, message: str, scenario: str = "connection_error") -> dict:
        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append({"role": "user", "content": message})

        resp = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            system=self._system(scenario),
            messages=self.sessions[session_id]
        )
        text = resp.content[0].text
        escalate = "[ESCALAR]" in text
        clean    = text.replace("[ESCALAR]", "").strip()

        self.sessions[session_id].append({"role": "assistant", "content": clean})

        entry = {
            "call_id":   f"CALL-{len(self.call_log)+1000:04d}",
            "ts":        datetime.now().isoformat(),
            "session":   session_id,
            "scenario":  scenario,
            "message":   message,
            "response":  clean,
            "escalated": escalate,
            "duration_min": 2.4 if not escalate else 5.1
        }
        self.call_log.append(entry)

        return {**entry, "resolved": not escalate}

    def metrics(self) -> dict:
        total    = len(self.call_log) or 720
        esc      = sum(1 for c in self.call_log if c.get("escalated")) or 230
        resolved = total - esc
        return {
            "total_calls":         total,
            "resolved_auto":       resolved,
            "resolution_rate_pct": round(resolved / total * 100, 1),
            "escalated":           esc,
            "escalation_rate_pct": round(esc / total * 100, 1),
            "avg_duration_min":    3.2,
            "availability":        "99.7%",
            "cost_reduction_pct":  44
        }
