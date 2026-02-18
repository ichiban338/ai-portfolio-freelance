#!/usr/bin/env python3
# generate_all.py – Genera los 5 dashboards del portafolio de una vez
# Ejecutar desde la raiz: python generate_all.py

import subprocess, sys, os

projects = [
    ("P1 – Chatbot FAQ TrendStore",          "p1_chatbot_faq/src/generate_dashboard.py"),
    ("P2 – Contestadora AI TechSolve",        "p2_contestadora_soporte/src/generate_dashboard.py"),
    ("P3 – Dashboard KPI MegaMart",           "p3_dashboard_ventas/src/sales_dashboard.py"),
    ("P4 – Asistente Marketing DigitalPulse", "p4_asistente_marketing/src/campaign_dashboard.py"),
    ("P5 – Call Center ContactPro",           "p5_callcenter_analytics/src/callcenter_dashboard.py"),
]

print("\n" + "="*55)
print("  Portfolio AI — Generando todos los dashboards")
print("="*55 + "\n")

ok, fail = 0, 0
for name, script in projects:
    print(f"Generando: {name}...")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  OK\n")
        ok += 1
    else:
        print(f"  ERROR: {result.stderr.strip()}\n")
        fail += 1

print("="*55)
print(f"Completado: {ok}/5 dashboards generados", end="")
print(f"  |  {fail} errores" if fail else "  sin errores")
print("="*55)
