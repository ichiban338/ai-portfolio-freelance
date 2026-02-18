#!/usr/bin/env python3
# src/generate_dashboard.py – Dashboard Contestadora AI P2

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np, os

OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

BG, PANEL, BORDER = "#0B0F1A", "#131929", "#1E2A3A"
BLUE, GREEN, ORANGE, RED, YELLOW, PURPLE, MUTED, WHITE = (
    "#4A90E2","#2ECC71","#E67E22","#E74C3C","#F1C40F","#9B59B6","#7F8C8D","#ECF0F1"
)

def kpi(ax, title, val, sub, color):
    ax.set_facecolor(PANEL)
    for sp in ax.spines.values(): sp.set_edgecolor(color); sp.set_linewidth(2)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.78, title,  ha="center", fontsize=9,   color=MUTED,  transform=ax.transAxes)
    ax.text(0.5, 0.46, val,    ha="center", fontsize=18,  color=color,  transform=ax.transAxes, fontweight="bold")
    ax.text(0.5, 0.18, sub,    ha="center", fontsize=8,   color=MUTED,  transform=ax.transAxes)

def generate(path):
    fig = plt.figure(figsize=(20, 13))
    fig.patch.set_facecolor(BG)
    gs  = gridspec.GridSpec(4, 4, figure=fig, hspace=0.48, wspace=0.32,
                            top=0.91, bottom=0.05, left=0.04, right=0.97)

    fig.text(0.5, 0.965, "ARIA — Contestadora AI | TechSolve Soporte Tecnico",
             ha="center", fontsize=17, fontweight="bold", color=WHITE)
    fig.text(0.5, 0.944, "Periodo: Octubre 2024  |  720 llamadas  |  Disponibilidad: 99.7%",
             ha="center", fontsize=9, color=MUTED)

    # KPI Cards
    cards = [
        ("Llamadas/mes", "720",      "Total gestionadas",       BLUE),
        ("Resolucion",   "68%",      "Sin agente humano",       GREEN),
        ("Duracion Med", "3.2 min",  "Tiempo promedio",         ORANGE),
        ("Ahorro",       "44%",      "Reduccion costos soporte", YELLOW),
    ]
    for i,(t,v,s,c) in enumerate(cards):
        kpi(fig.add_subplot(gs[0,i]), t, v, s, c)

    # Llamadas por hora
    ax1 = fig.add_subplot(gs[1, :2])
    ax1.set_facecolor(PANEL)
    hours = list(range(8,20))
    calls = [18,42,68,75,58,38,35,55,72,61,42,24]
    bc    = [GREEN if h in [10,11,15,16] else "#1A2A3A" for h in hours]
    ax1.bar(hours, calls, color=bc, width=0.7, alpha=0.9)
    ax1.axhline(np.mean(calls), color=YELLOW, linestyle="--", alpha=0.5,
                linewidth=1.2, label=f"Prom: {np.mean(calls):.0f}/hr")
    ax1.set_title("Volumen de Llamadas por Hora", color=WHITE, fontsize=12, pad=8, loc="left")
    ax1.set_xlabel("Hora", color=MUTED, fontsize=9)
    ax1.set_ylabel("Llamadas", color=MUTED, fontsize=9)
    ax1.tick_params(colors=MUTED, labelsize=9)
    for sp in ["top","right"]: ax1.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax1.spines[sp].set_color(BORDER)
    ax1.legend(fontsize=8, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL)

    # Distribucion por problema
    ax2 = fig.add_subplot(gs[1, 2:])
    ax2.set_facecolor(PANEL)
    probs  = ["Conexion", "Reset Password", "Facturacion", "Instalacion", "Otros"]
    pcts   = [42, 35, 15, 5, 3]
    colors = [BLUE, GREEN, ORANGE, PURPLE, MUTED]
    bars   = ax2.barh(probs, pcts, color=colors, height=0.55, alpha=0.9)
    for b,v in zip(bars,pcts):
        ax2.text(v+0.4, b.get_y()+b.get_height()/2, f"{v}%", va="center", fontsize=9, color=WHITE)
    ax2.set_title("Distribucion por Tipo de Problema", color=WHITE, fontsize=12, pad=8, loc="left")
    ax2.set_xlabel("% del total", color=MUTED, fontsize=9)
    ax2.tick_params(colors=MUTED, labelsize=9)
    for sp in ["top","right"]: ax2.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax2.spines[sp].set_color(BORDER)

    # Tasa resolucion por tipo
    ax3 = fig.add_subplot(gs[2, :2])
    ax3.set_facecolor(PANEL)
    res_types = ["Facturacion", "Reset Pass", "Info General", "Conexion", "Instalacion"]
    res_vals  = [88, 82, 95, 55, 48]
    rc        = [GREEN if v>=70 else ORANGE if v>=50 else RED for v in res_vals]
    brs       = ax3.bar(res_types, res_vals, color=rc, width=0.55, alpha=0.9)
    ax3.axhline(70, color=WHITE, linestyle="--", alpha=0.35, linewidth=1.2, label="Objetivo 70%")
    ax3.set_ylim(0,115)
    ax3.set_title("Tasa de Resolucion Automatica por Tipo", color=WHITE, fontsize=11, pad=8, loc="left")
    ax3.set_ylabel("% Resuelto", color=MUTED, fontsize=9)
    ax3.tick_params(colors=MUTED, labelsize=8.5, axis="x", rotation=12)
    ax3.tick_params(colors=MUTED, labelsize=9, axis="y")
    for sp in ["top","right"]: ax3.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax3.spines[sp].set_color(BORDER)
    ax3.legend(fontsize=8, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL)
    for b,v in zip(brs,res_vals):
        ax3.text(b.get_x()+b.get_width()/2, v+1, f"{v}%", ha="center", fontsize=9, color=WHITE, fontweight="bold")

    # Tendencia semanal
    ax4 = fig.add_subplot(gs[2, 2:])
    ax4.set_facecolor(PANEL)
    np.random.seed(5)
    weeks = [f"Sem {i+1}" for i in range(8)]
    auto  = [68,71,66,74,70,69,72,68]
    escl  = [32,29,34,26,30,31,28,32]
    x = np.arange(len(weeks))
    ax4.bar(x, auto, label="Resuelto auto", color=GREEN, alpha=0.85, width=0.5)
    ax4.bar(x, escl, bottom=auto, label="Escalado", color=ORANGE, alpha=0.85, width=0.5)
    ax4.set_xticks(x); ax4.set_xticklabels(weeks, fontsize=8.5)
    ax4.set_title("Resolucion vs Escalacion Semanal (%)", color=WHITE, fontsize=11, pad=8, loc="left")
    ax4.set_ylabel("Porcentaje", color=MUTED, fontsize=9)
    ax4.tick_params(colors=MUTED, labelsize=9)
    for sp in ["top","right"]: ax4.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax4.spines[sp].set_color(BORDER)
    ax4.legend(fontsize=8.5, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL)

    # Canal de contacto
    ax5 = fig.add_subplot(gs[3, 0])
    ax5.set_facecolor(PANEL)
    ax5.pie([60,25,15], labels=["IVR Voz","SMS","WhatsApp"],
            colors=[BLUE,GREEN,PURPLE], autopct="%1.0f%%",
            wedgeprops={"linewidth":2,"edgecolor":BG},
            textprops={"color":WHITE,"fontsize":9}, startangle=90)
    ax5.set_title("Canal de Contacto", color=WHITE, fontsize=10, pad=6)

    # Satisfaccion
    ax6 = fig.add_subplot(gs[3, 1:3])
    ax6.set_facecolor(PANEL)
    np.random.seed(3)
    days  = np.arange(1,31)
    sat   = np.clip(np.random.normal(3.8, 0.35, 30), 2.5, 5.0)
    ax6.fill_between(days, sat, alpha=0.2, color=GREEN)
    ax6.plot(days, sat, color=GREEN, linewidth=2)
    ax6.axhline(4.0, color=YELLOW, linestyle="--", alpha=0.5, linewidth=1.2, label="Objetivo 4.0")
    ax6.set_ylim(1,5.5)
    ax6.set_title("Satisfaccion Diaria del Cliente (CSAT)", color=WHITE, fontsize=11, pad=8, loc="left")
    ax6.set_xlabel("Dia del mes", color=MUTED, fontsize=8.5)
    ax6.set_ylabel("Puntuacion", color=MUTED, fontsize=8.5)
    ax6.tick_params(colors=MUTED, labelsize=8.5)
    for sp in ["top","right"]: ax6.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax6.spines[sp].set_color(BORDER)
    ax6.legend(fontsize=8, framealpha=0.2, labelcolor=WHITE, facecolor=PANEL)

    # Insight
    ax7 = fig.add_subplot(gs[3, 3])
    ax7.set_facecolor(PANEL)
    for sp in ax7.spines.values(): sp.set_edgecolor(ORANGE); sp.set_linewidth(2)
    ax7.set_xticks([]); ax7.set_yticks([])
    ax7.text(0.5, 0.5,
             "OPORTUNIDAD\n\n"
             "Instalacion y\n"
             "Conexion tienen\n"
             "resolucion <55%.\n\n"
             "Agregar guias\n"
             "paso a paso\n"
             "puede subir\n"
             "al 70%.",
             ha="center", va="center", fontsize=8.5, color=WHITE,
             transform=ax7.transAxes, linespacing=1.7)

    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close()
    print(f"Dashboard guardado: {path}")

if __name__ == "__main__":
    generate(os.path.join(OUT, "dashboard_p2_contestadora.png"))
