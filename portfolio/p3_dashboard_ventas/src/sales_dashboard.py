#!/usr/bin/env python3
# ============================================================
# src/sales_dashboard.py – KPI Ventas para MegaMart
# Proyecto 3: Dashboard interactivo de ventas retail
# ============================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta

OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

BG, PANEL, BORDER = "#070B14", "#0E1525", "#182135"
BLUE   = "#4A8FE7"
GREEN  = "#27AE60"
ORANGE = "#E67E22"
RED    = "#E74C3C"
GOLD   = "#F1C40F"
PURPLE = "#8E44AD"
TEAL   = "#1ABC9C"
MUTED  = "#6C7A89"
WHITE  = "#ECF0F1"

# ── Generador de datos ───────────────────────────────────────
def make_data(n_months=6):
    np.random.seed(42)
    branches   = ["Norte Centro","Sur Poniente","Este Plaza","Oeste Mall",
                  "Centro Hist.","Pedregal","Satelite","Coyoacan",
                  "Polanco","Tlalpan","Iztapalapa","Xochimilco"]
    categories = {"Calzado Deportivo":2800,"Ropa Casual":1200,
                  "Ropa Deportiva":1800,"Accesorios":450,
                  "Calzado Formal":3200,"Mochilas":890}

    rows = []
    base = datetime.now() - timedelta(days=n_months*30)
    for branch in branches:
        bf = np.random.uniform(0.7,1.4)
        for d in range(n_months*30):
            date = base + timedelta(days=d)
            wf   = 1.4 if date.weekday()>=5 else 1.0
            for _ in range(int(np.random.poisson(25*bf*wf))):
                cat   = np.random.choice(list(categories.keys()),
                                         p=[v/sum(categories.values()) for v in categories.values()])
                price = categories[cat] * np.random.uniform(0.85,1.15)
                qty   = np.random.choice([1,2,3], p=[0.70,0.22,0.08])
                disc  = np.random.choice([0,.05,.10,.15,.20], p=[.55,.20,.15,.07,.03])
                rows.append({
                    "date":     date,
                    "branch":   branch,
                    "category": cat,
                    "qty":      qty,
                    "price":    price,
                    "discount": disc,
                    "revenue":  round(price*(1-disc)*qty, 2),
                    "month":    date.strftime("%b %Y")
                })
    return pd.DataFrame(rows)

# ── Dashboard principal ──────────────────────────────────────
def generate(path):
    df = make_data()
    df["date"] = pd.to_datetime(df["date"])

    # KPIs del mes más reciente
    last_month  = df["date"].dt.to_period("M").max()
    prev_month  = last_month - 1
    cur  = df[df["date"].dt.to_period("M") == last_month]
    prev = df[df["date"].dt.to_period("M") == prev_month]

    rev_cur  = cur["revenue"].sum()
    rev_prev = prev["revenue"].sum()
    pct_chg  = (rev_cur - rev_prev) / rev_prev * 100

    top_branch  = cur.groupby("branch")["revenue"].sum().idxmax()
    top_rev     = cur.groupby("branch")["revenue"].sum().max()
    units_cur   = int(cur["qty"].sum())

    # ── Figure ──────────────────────────────────────────────
    fig = plt.figure(figsize=(22, 14))
    fig.patch.set_facecolor(BG)
    gs  = gridspec.GridSpec(4, 4, figure=fig, hspace=0.46, wspace=0.32,
                            top=0.91, bottom=0.05, left=0.04, right=0.97)

    fig.text(0.5, 0.965, "MegaMart — Dashboard KPI Ventas | 12 Sucursales",
             ha="center", fontsize=18, fontweight="bold", color=WHITE)
    fig.text(0.5, 0.944, f"Periodo: 6 meses  |  Actualizado: {datetime.now().strftime('%d/%b/%Y')}  |  12 sucursales  |  6 categorias",
             ha="center", fontsize=9, color=MUTED)

    # KPI Cards
    def kpi(ax, title, val, sub, color):
        ax.set_facecolor(PANEL)
        for sp in ax.spines.values(): sp.set_edgecolor(color); sp.set_linewidth(2.5)
        ax.set_xticks([]); ax.set_yticks([])
        ax.text(0.5,0.78,title, ha="center",fontsize=9,  color=MUTED, transform=ax.transAxes)
        ax.text(0.5,0.46,val,   ha="center",fontsize=17, color=color, transform=ax.transAxes,fontweight="bold")
        ax.text(0.5,0.17,sub,   ha="center",fontsize=8,  color=MUTED, transform=ax.transAxes)

    sign = "+" if pct_chg >= 0 else ""
    kpi(fig.add_subplot(gs[0,0]), "Ventas del Mes",    f"${rev_cur/1e6:.2f}M",  f"{sign}{pct_chg:.1f}% vs mes ant.", GREEN if pct_chg>=0 else RED)
    kpi(fig.add_subplot(gs[0,1]), "Unidades Vendidas", f"{units_cur:,}",         "Unidades en el mes",                BLUE)
    kpi(fig.add_subplot(gs[0,2]), "Sucursal Lider",    top_branch,               f"${top_rev/1e3:.0f}K en ventas",    GOLD)
    kpi(fig.add_subplot(gs[0,3]), "Conversion Prom",   "7.2%",                   "Meta: 7.0%",                        TEAL)

    # Ventas mensuales por categoría (stacked bar)
    ax1 = fig.add_subplot(gs[1:3, :2])
    ax1.set_facecolor(PANEL)
    monthly = df.groupby([df["date"].dt.to_period("M").astype(str), "category"])["revenue"].sum().unstack(fill_value=0)
    months  = monthly.index.tolist()
    cats    = monthly.columns.tolist()
    clrs    = [BLUE, GREEN, ORANGE, PURPLE, TEAL, GOLD]
    bottom  = np.zeros(len(months))
    for idx, cat in enumerate(cats):
        vals = monthly[cat].values
        ax1.bar(months, vals, bottom=bottom, label=cat[:14], color=clrs[idx%len(clrs)], alpha=0.85, width=0.6)
        bottom += vals
    ax1.set_title("Ventas Mensuales por Categoria", color=WHITE, fontsize=12, pad=10, loc="left")
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f"${x/1e6:.1f}M"))
    ax1.tick_params(colors=MUTED, labelsize=8.5, axis="x", rotation=18)
    ax1.tick_params(colors=MUTED, labelsize=8.5, axis="y")
    for sp in ["top","right"]: ax1.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax1.spines[sp].set_color(BORDER)
    ax1.legend(fontsize=7.5, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL, loc="upper left")
    ax1.grid(axis="y", color=BORDER, alpha=0.5)

    # Top sucursales (horizontal bar)
    ax2 = fig.add_subplot(gs[1, 2:])
    ax2.set_facecolor(PANEL)
    branch_sales = df.groupby("branch")["revenue"].sum().sort_values(ascending=True).tail(8)
    bc = [BLUE if i==len(branch_sales)-1 else "#1E3050" for i in range(len(branch_sales))]
    ax2.barh(range(len(branch_sales)), branch_sales.values, color=bc, height=0.6, alpha=0.9)
    ax2.set_yticks(range(len(branch_sales)))
    ax2.set_yticklabels(branch_sales.index, fontsize=8.5, color=WHITE)
    ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f"${x/1e6:.1f}M"))
    ax2.set_title("Ventas Totales por Sucursal", color=WHITE, fontsize=11, pad=8, loc="left")
    ax2.tick_params(colors=MUTED, labelsize=8.5)
    for sp in ["top","right"]: ax2.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax2.spines[sp].set_color(BORDER)
    ax2.grid(axis="x", color=BORDER, alpha=0.5)
    for i,v in enumerate(branch_sales.values):
        ax2.text(v*1.01, i, f"${v/1e6:.2f}M", va="center", fontsize=7.5, color=MUTED)

    # Metodos de pago
    ax3 = fig.add_subplot(gs[2, 2])
    ax3.set_facecolor(PANEL)
    ax3.pie([55,30,15], labels=["Tarjeta","Efectivo","Digital"],
            colors=[BLUE,GREEN,PURPLE], autopct="%1.0f%%",
            wedgeprops={"linewidth":2,"edgecolor":BG},
            textprops={"color":WHITE,"fontsize":9}, startangle=90)
    ax3.set_title("Metodo de Pago", color=WHITE, fontsize=11, pad=6)

    # Tipo de cliente
    ax4 = fig.add_subplot(gs[2, 3])
    ax4.set_facecolor(PANEL)
    ax4.pie([38,45,17], labels=["Nuevo","Recurrente","VIP"],
            colors=[ORANGE,TEAL,GOLD], autopct="%1.0f%%",
            wedgeprops={"linewidth":2,"edgecolor":BG},
            textprops={"color":WHITE,"fontsize":9}, startangle=140)
    ax4.set_title("Tipo de Cliente", color=WHITE, fontsize=11, pad=6)

    # Alertas de stock (fila 3)
    ax5 = fig.add_subplot(gs[3, :])
    ax5.set_facecolor("#0E1A10")
    for sp in ax5.spines.values(): sp.set_edgecolor(ORANGE); sp.set_linewidth(1.5)
    ax5.set_xticks([]); ax5.set_yticks([])

    ax5.text(0.01, 0.88, "ALERTAS DE INVENTARIO — Productos en Riesgo de Quiebre de Stock",
             va="top", fontsize=11, fontweight="bold", color=ORANGE, transform=ax5.transAxes)

    alerts = [
        ("Runner Pro X",   8,  RED,    "CRITICO"),
        ("Oxford Ejecut.", 11, RED,    "CRITICO"),
        ("Shorts Dry-Fit", 14, ORANGE, "BAJO"),
        ("Cap Logo",       16, ORANGE, "BAJO"),
        ("Tote Canvas",    19, ORANGE, "BAJO"),
        ("Jeans Slim Fit", 22, ORANGE, "BAJO"),
        ("Loafer Business",25, GOLD,   "REVISAR"),
        ("Sneaker Classic",28, GOLD,   "REVISAR"),
    ]
    xs = np.linspace(0.03, 0.97, len(alerts))
    for (name, stock, c, status), x in zip(alerts, xs):
        ax5.add_patch(plt.Rectangle((x-0.055, 0.05), 0.105, 0.72,
                                    facecolor=BG, edgecolor=c, linewidth=1.5,
                                    transform=ax5.transAxes))
        ax5.text(x, 0.64, name,    ha="center", fontsize=7.5,  color=WHITE,  transform=ax5.transAxes)
        ax5.text(x, 0.46, f"{stock} u.", ha="center", fontsize=10, color=c, fontweight="bold", transform=ax5.transAxes)
        ax5.text(x, 0.25, status,  ha="center", fontsize=8,   color=c,     transform=ax5.transAxes)

    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close()
    print(f"Dashboard guardado: {path}")

if __name__ == "__main__":
    generate(os.path.join(OUT, "dashboard_p3_ventas.png"))
