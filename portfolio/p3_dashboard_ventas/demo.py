#!/usr/bin/env python3
# demo.py – Genera dashboard y reporte Excel de MegaMart
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from sales_dashboard import make_data, generate, OUT

def run():
    print("\n" + "="*55)
    print("  MegaMart — Dashboard KPI Ventas | Demo")
    print("="*55)
    print("\nGenerando datos simulados (12 sucursales, 6 meses)...")
    df = make_data()
    print(f"  {len(df):,} registros de venta generados")
    print("\nGenerando dashboard visual...")
    path = os.path.join(OUT, "dashboard_p3_ventas.png")
    generate(path)
    print(f"\nListo. Abre el archivo: {path}")

if __name__ == "__main__":
    run()
