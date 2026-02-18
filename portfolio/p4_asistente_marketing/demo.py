#!/usr/bin/env python3
# demo.py – Demo asistente marketing DigitalPulse
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from campaign_dashboard import generate, OUT

def run():
    print("\n" + "="*55)
    print("  DigitalPulse — Asistente AI Marketing | Demo")
    print("="*55)
    print("\nGenerando dashboard de campanas...")
    path = os.path.join(OUT, "dashboard_p4_marketing.png")
    generate(path)
    print(f"\nListo. Abre el archivo: {path}")

if __name__ == "__main__":
    run()
