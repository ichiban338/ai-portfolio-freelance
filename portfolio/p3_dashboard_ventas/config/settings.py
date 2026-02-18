# config/settings.py – Dashboard KPI MegaMart
import os

N_MONTHS   = 6       # Meses de datos a generar
N_BRANCHES = 12      # Numero de sucursales
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
