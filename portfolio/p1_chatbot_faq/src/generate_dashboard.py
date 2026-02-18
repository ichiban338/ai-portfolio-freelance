#!/usr/bin/env python3
# ============================================================
# src/generate_dashboard.py – Dashboard visual de métricas
# Ejecutar: python src/generate_dashboard.py
# ============================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

# ── Paleta ──────────────────────────────────────────────────
BG      = "#0D1117"
PANEL   = "#161B22"
BORDER  = "#21262D"
BLUE    = "#4F8EF7"
GREEN   = "#3FB950"
ORANGE  = "#F78166"
YELLOW  = "#E3B341"
PURPLE  = "#BC8CFF"
TEAL    = "#39D353"
MUTED   = "#8B949E"
WHITE   = "#F0F6FC"

def kpi_card(ax, title, value, subtitle, color):
    ax.set_facecolor(PANEL)
    for sp in ax.spines.values():
        sp.set_edgecolor(color); sp.set_linewidth(2)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.78, title,  ha="center", fontsize=9,   color=MUTED,  transform=ax.transAxes)
    ax.text(0.5, 0.47, value,  ha="center", fontsize=19,  color=color,  transform=ax.transAxes, fontweight="bold")
    ax.text(0.5, 0.18, subtitle, ha="center", fontsize=8, color=MUTED,  transform=ax.transAxes)

def generate(path: str):
    fig = plt.figure(figsize=(20, 13))
    fig.patch.set_facecolor(BG)

    gs = gridspec.GridSpec(4, 4, figure=fig,
                           hspace=0.48, wspace=0.32,
                           top=0.91, bottom=0.05, left=0.04, right=0.97)

    # Header
    fig.text(0.5, 0.965, "💬  Sofia FAQ Bot — Dashboard de Métricas | TrendStore",
             ha="center", fontsize=17, fontweight="bold", color=WHITE)
    fig.text(0.5, 0.944, "Período: Octubre 2024  ·  1,240 interacciones  ·  Actualizado hoy",
             ha="center", fontsize=9, color=MUTED)

    # ── KPI Cards (fila 0) ──────────────────────────────────
    cards = [
        ("💬 Interacciones", "1,240",    "Consultas gestionadas/mes", BLUE),
        ("✅ Resolución",    "74%",       "Sin intervención humana",   GREEN),
        ("⭐ CSAT",          "4.4 / 5",  "Satisfacción del cliente",  YELLOW),
        ("⚡ Resp. Media",   "2.1 seg",   "Tiempo de respuesta",       PURPLE),
    ]
    for i, (t, v, s, c) in enumerate(cards):
        kpi_card(fig.add_subplot(gs[0, i]), t, v, s, c)

    # ── Distribución de consultas (barras horizontales) ─────
    ax1 = fig.add_subplot(gs[1:3, 0:2])
    ax1.set_facecolor(PANEL)

    cats   = ["Envíos", "Estado Pedidos", "Devoluciones", "Productos", "Pagos", "Otros"]
    values = [31, 24, 22, 15, 5, 3]
    colors = [BLUE, PURPLE, ORANGE, GREEN, TEAL, MUTED]
    y_pos  = range(len(cats))

    bars = ax1.barh(y_pos, values, color=colors, height=0.55, alpha=0.9)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(cats, fontsize=10, color=WHITE)
    ax1.set_xlabel("% del total de consultas", color=MUTED, fontsize=9)
    ax1.set_title("Distribución de Consultas por Categoría",
                  color=WHITE, fontsize=12, pad=10, loc="left")
    ax1.tick_params(colors=MUTED, labelsize=9)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    for sp in ["bottom", "left"]:
        ax1.spines[sp].set_color(BORDER)
    ax1.grid(axis="x", color=BORDER, alpha=0.6)

    for bar, val in zip(bars, values):
        ax1.text(val + 0.4, bar.get_y() + bar.get_height()/2,
                 f"{val}%", va="center", fontsize=9.5, color=WHITE)

    # ── Tendencia de interacciones diarias ──────────────────
    ax2 = fig.add_subplot(gs[1, 2:])
    ax2.set_facecolor(PANEL)

    np.random.seed(7)
    days = np.arange(1, 31)
    daily = np.clip(np.random.poisson(41, 30) + np.sin(days * 0.3) * 6, 20, 75).astype(int)

    ax2.fill_between(days, daily, alpha=0.25, color=BLUE)
    ax2.plot(days, daily, color=BLUE, linewidth=2)
    ax2.axhline(daily.mean(), color=YELLOW, linestyle="--", alpha=0.6,
                linewidth=1.2, label=f"Promedio: {daily.mean():.0f}/día")
    ax2.set_title("Interacciones Diarias – Octubre", color=WHITE, fontsize=11, pad=8, loc="left")
    ax2.set_xlabel("Día del mes", color=MUTED, fontsize=8.5)
    ax2.set_ylabel("N° de consultas", color=MUTED, fontsize=8.5)
    ax2.tick_params(colors=MUTED, labelsize=8)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    for sp in ["bottom", "left"]:
        ax2.spines[sp].set_color(BORDER)
    ax2.legend(fontsize=8, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL)

    # ── CSAT por categoría ──────────────────────────────────
    ax3 = fig.add_subplot(gs[2, 2:])
    ax3.set_facecolor(PANEL)

    csat_cats  = ["Envíos", "Pedidos", "Devoluciones", "Productos", "Pagos"]
    csat_vals  = [4.5, 4.4, 4.1, 4.6, 4.3]
    csat_colors = [GREEN if v >= 4.3 else ORANGE for v in csat_vals]

    ax3.bar(csat_cats, csat_vals, color=csat_colors, width=0.5, alpha=0.9)
    ax3.axhline(4.0, color=YELLOW, linestyle="--", alpha=0.5, linewidth=1.2, label="Objetivo (4.0)")
    ax3.set_ylim(3.0, 5.2)
    ax3.set_title("CSAT por Categoría de Consulta", color=WHITE, fontsize=11, pad=8, loc="left")
    ax3.set_ylabel("Puntuación", color=MUTED, fontsize=8.5)
    ax3.tick_params(colors=MUTED, labelsize=9)
    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)
    for sp in ["bottom", "left"]:
        ax3.spines[sp].set_color(BORDER)
    ax3.legend(fontsize=8, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL)
    for i, v in enumerate(csat_vals):
        ax3.text(i, v + 0.04, f"⭐{v}", ha="center", fontsize=8.5, color=WHITE)

    # ── Donut: Resolución vs Escalación ─────────────────────
    ax4 = fig.add_subplot(gs[3, 0])
    ax4.set_facecolor(PANEL)
    wedges, texts, autotexts = ax4.pie(
        [74, 26], labels=["Resuelto (74%)", "Escalado (26%)"],
        colors=[GREEN, ORANGE], startangle=90,
        wedgeprops={"linewidth": 2, "edgecolor": BG},
        autopct="%1.0f%%",
        textprops={"color": WHITE, "fontsize": 9}
    )
    ax4.set_title("Resolución vs Escalación", color=WHITE, fontsize=10, pad=6)

    # ── Consultas por hora del día ───────────────────────────
    ax5 = fig.add_subplot(gs[3, 1:3])
    ax5.set_facecolor(PANEL)

    hours  = list(range(8, 21))
    hourly = [12, 28, 52, 61, 48, 35, 42, 58, 64, 55, 38, 22, 14]
    bar_c  = [BLUE if h in [10, 11, 14, 15] else "#2D3A5F" for h in hours]

    ax5.bar(hours, hourly, color=bar_c, width=0.7, alpha=0.9)
    ax5.set_title("Consultas por Hora del Día", color=WHITE, fontsize=11, pad=8, loc="left")
    ax5.set_xlabel("Hora", color=MUTED, fontsize=8.5)
    ax5.set_ylabel("Consultas", color=MUTED, fontsize=8.5)
    ax5.tick_params(colors=MUTED, labelsize=8.5)
    ax5.spines["top"].set_visible(False)
    ax5.spines["right"].set_visible(False)
    for sp in ["bottom", "left"]:
        ax5.spines[sp].set_color(BORDER)

    # ── Insight box ─────────────────────────────────────────
    ax6 = fig.add_subplot(gs[3, 3])
    ax6.set_facecolor(PANEL)
    for sp in ax6.spines.values():
        sp.set_edgecolor(YELLOW); sp.set_linewidth(2)
    ax6.set_xticks([]); ax6.set_yticks([])

    insight = (
        "💡 INSIGHT CLAVE\n\n"
        "Pico de consultas:\n"
        "10–11 hrs y 14–15 hrs\n\n"
        "Oportunidad:\n"
        "Reducir el 26% de\n"
        "escalaciones con\n"
        "respuestas de cuenta\n"
        "más detalladas."
    )
    ax6.text(0.5, 0.5, insight, ha="center", va="center",
             fontsize=8.5, color=WHITE, transform=ax6.transAxes,
             linespacing=1.7)

    plt.savefig(path, dpi=150, bbox_inches="tight",
                facecolor=BG, edgecolor="none")
    plt.close()
    print(f"✅ Dashboard guardado: {path}")

if __name__ == "__main__":
    generate(os.path.join(OUT, "dashboard_p1_chatbot.png"))
