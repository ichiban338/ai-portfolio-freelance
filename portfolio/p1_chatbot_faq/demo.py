#!/usr/bin/env python3
# ============================================================
# demo.py – Demo interactivo en terminal (sin API key)
# Ejecutar: python demo.py
# ============================================================

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from chatbot_engine import ChatBotEngine
from datetime import datetime

DEMO_SCRIPT = [
    "¿Cuánto tarda el envío estándar?",
    "¿Cuándo es el envío gratis?",
    "Quiero devolver un producto que compré hace 2 semanas",
    "¿Cómo hago seguimiento de mi pedido?",
    "¿Tienen tallas grandes disponibles?",
    "¿Qué métodos de pago aceptan?",
]

def run_demo():
    print("\n" + "═"*60)
    print("  🛍️  SOFIA – Asistente Virtual TrendStore")
    print("  Chatbot FAQ Inteligente | Demo Interactivo")
    print("═"*60)
    print("Comandos: 'auto' = demo guiado | 'reporte' = métricas | 'salir'\n")

    bot        = ChatBotEngine()   # sin API key → modo stub
    session_id = f"demo_{datetime.now().strftime('%H%M%S')}"
    mode       = input("Modo (auto/manual) [auto]: ").strip().lower() or "auto"

    if mode == "auto":
        for question in DEMO_SCRIPT:
            print(f"\n👤 Cliente: {question}")
            result = bot.chat(session_id, question)
            print(f"🤖 Sofia:   {result['response']}")
            print(f"           ⏱  Turno #{result['turn_number']}")
        _print_metrics(bot)
    else:
        while True:
            user_input = input("\nTú: ").strip()
            if not user_input:
                continue
            if user_input.lower() == "salir":
                _print_metrics(bot)
                break
            if user_input.lower() == "reporte":
                _print_metrics(bot)
                continue
            result = bot.chat(session_id, user_input)
            print(f"Sofia: {result['response']}")

def _print_metrics(bot: ChatBotEngine):
    m = bot.get_metrics()
    print("\n" + "─"*50)
    print("📊 MÉTRICAS DE LA SESIÓN")
    print(f"   Interacciones:        {m['total_interactions']}")
    print(f"   Tasa de resolución:   {m['resolution_rate_pct']}%")
    print(f"   CSAT simulado:        {m['simulated_csat']}/5.0")
    print(f"   Reducción de soporte: {m['support_load_reduction']}")
    print("─"*50)

if __name__ == "__main__":
    run_demo()
