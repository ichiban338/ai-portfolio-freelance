#!/usr/bin/env python3
# demo.py – Demo ContactPro Call Center AI
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from callcenter_dashboard import make_call_data, generate, OUT

def run():
    print("\n" + "="*55)
    print("  ContactPro — Call Center AI | Demo")
    print("="*55)
    print("\nGenerando datos de interacciones simuladas...")
    df = make_call_data(500)
    print(f"  {len(df):,} interacciones generadas")
    res = df["resolved"].sum()
    print(f"  Resolucion automatica: {res/len(df)*100:.0f}% ({res} casos)")
    print("\nGenerando dashboard operacional...")
    path = os.path.join(OUT, "dashboard_p5_callcenter.png")
    generate(path)
    print(f"\nListo. Abre el archivo: {path}")

if __name__ == "__main__":
    run()
