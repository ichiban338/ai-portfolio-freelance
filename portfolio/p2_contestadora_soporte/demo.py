#!/usr/bin/env python3
# demo.py – Demo contestadora TechSolve (sin Twilio ni API key)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from voice_operator import VoiceOperator

SCENARIOS = [
    ("password_reset",   "No puedo entrar a mi cuenta, olvide mi contrasena"),
    ("connection_error", "Me aparece el error ERR_002 y no puedo trabajar"),
    ("billing",          "Necesito la factura del mes pasado"),
    ("connection_error", "La aplicacion no carga, intente todo y nada funciona"),
]

def run():
    print("\n" + "="*60)
    print("  ARIA — Contestadora AI TechSolve | Demo")
    print("="*60)
    op = VoiceOperator()
    for i, (scenario, message) in enumerate(SCENARIOS, 1):
        print(f"\n[Llamada {i}] Escenario: {scenario}")
        print(f"Cliente: {message}")
        result = op.process(f"SES-{i:03d}", message, scenario)
        print(f"ARIA:    {result['response']}")
        status = "RESUELTO" if result["resolved"] else "-> ESCALADO AL AGENTE"
        print(f"         [{status}]")
        print("-"*50)
    m = op.metrics()
    print(f"\nResumen: {m['total_calls']} llamadas | Resolucion: {m['resolution_rate_pct']}%")

if __name__ == "__main__":
    run()
