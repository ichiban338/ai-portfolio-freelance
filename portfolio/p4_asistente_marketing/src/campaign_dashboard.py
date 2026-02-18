#!/usr/bin/env python3
# src/campaign_dashboard.py – DigitalPulse Agency

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker
import numpy as np
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

BG, PANEL, BORDER = "#080C18","#0F1628","#182040"
BLUE,GREEN,ORANGE,RED,GOLD,PURPLE,TEAL,MUTED,WHITE = (
    "#4A8FE7","#2ECC71","#E67E22","#E74C3C",
    "#F1C40F","#9B59B6","#1ABC9C","#6C7A89","#ECF0F1"
)

def kpi(ax,title,val,sub,color):
    ax.set_facecolor(PANEL)
    for sp in ax.spines.values(): sp.set_edgecolor(color); sp.set_linewidth(2.5)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5,0.78,title, ha="center",fontsize=9,  color=MUTED, transform=ax.transAxes)
    ax.text(0.5,0.46,val,   ha="center",fontsize=18, color=color, transform=ax.transAxes,fontweight="bold")
    ax.text(0.5,0.17,sub,   ha="center",fontsize=8,  color=MUTED, transform=ax.transAxes)

np.random.seed(99)
CLIENTS = ["FreshMart","TechNova","FitLife","LuxHome","EduPro"]
CHANNELS= ["Meta Ads","Google Ads","Email Mktg","TikTok"]
BUDGETS = [8500,15000,5500,22000,7200]
ROAS    = [3.2,4.1,2.8,5.3,3.7]
CTR     = [3.2,4.8,2.8,5.5,3.8]

def generate(path):
    fig = plt.figure(figsize=(21,14))
    fig.patch.set_facecolor(BG)
    gs  = gridspec.GridSpec(4,4,figure=fig,hspace=0.46,wspace=0.32,
                            top=0.91,bottom=0.05,left=0.04,right=0.97)

    fig.text(0.5,0.965,"DigitalPulse Agency — Dashboard de Campanas | 5 Clientes",
             ha="center",fontsize=17,fontweight="bold",color=WHITE)
    fig.text(0.5,0.944,"Periodo: Octubre 2024  |  4 Canales  |  35 reportes generados automaticamente",
             ha="center",fontsize=9,color=MUTED)

    # KPI Cards
    total_inv = sum(BUDGETS)
    total_rev = sum(b*r for b,r in zip(BUDGETS,ROAS))
    avg_roas  = total_rev/total_inv
    kpi(fig.add_subplot(gs[0,0]),"Inversion Total",   f"${total_inv/1e3:.0f}K",  "5 clientes activos", BLUE)
    kpi(fig.add_subplot(gs[0,1]),"Ingresos Generados",f"${total_rev/1e3:.0f}K",  "Periodo del mes",    GREEN)
    kpi(fig.add_subplot(gs[0,2]),"ROAS Promedio",     f"{avg_roas:.1f}x",         "Benchmark: 3.5x",    GOLD if avg_roas>=3.5 else RED)
    kpi(fig.add_subplot(gs[0,3]),"Reportes Auto",     "35 / mes",                 "Sin intervencion manual",TEAL)

    # ROAS por cliente
    ax1 = fig.add_subplot(gs[1,:2])
    ax1.set_facecolor(PANEL)
    bc = [GREEN if r>=3.5 else ORANGE if r>=2.5 else RED for r in ROAS]
    bars = ax1.bar(CLIENTS, ROAS, color=bc, width=0.55, alpha=0.9)
    ax1.axhline(3.5,color=WHITE,linestyle="--",alpha=0.35,linewidth=1.2,label="Benchmark 3.5x")
    ax1.set_title("ROAS por Cliente",color=WHITE,fontsize=12,pad=8,loc="left")
    ax1.set_ylabel("ROAS (x)",color=MUTED,fontsize=9)
    ax1.tick_params(colors=MUTED,labelsize=9)
    for sp in ["top","right"]: ax1.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax1.spines[sp].set_color(BORDER)
    ax1.legend(fontsize=8,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL)
    for b,v in zip(bars,ROAS):
        ax1.text(b.get_x()+b.get_width()/2,v+0.05,f"{v}x",
                 ha="center",fontsize=9.5,color=WHITE,fontweight="bold")

    # Inversion vs Ingresos
    ax2 = fig.add_subplot(gs[1,2:])
    ax2.set_facecolor(PANEL)
    x = np.arange(len(CLIENTS))
    w = 0.35
    revenues = [b*r for b,r in zip(BUDGETS,ROAS)]
    ax2.bar(x-w/2, BUDGETS,  w, color=BLUE,  alpha=0.85, label="Invertido")
    ax2.bar(x+w/2, revenues, w, color=GREEN, alpha=0.85, label="Ingresos")
    ax2.set_xticks(x); ax2.set_xticklabels([c[:8] for c in CLIENTS],rotation=20,fontsize=8.5)
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v/1e3:.0f}K"))
    ax2.set_title("Inversion vs Ingresos por Cliente",color=WHITE,fontsize=12,pad=8,loc="left")
    ax2.tick_params(colors=MUTED,labelsize=8.5)
    for sp in ["top","right"]: ax2.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax2.spines[sp].set_color(BORDER)
    ax2.legend(fontsize=8.5,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL)

    # CTR por canal
    ax3 = fig.add_subplot(gs[2,:2])
    ax3.set_facecolor(PANEL)
    ctr_vals = [3.2, 4.8, 2.8, 5.5]
    ch_clrs  = [BLUE, GREEN, ORANGE, PURPLE]
    ax3.barh(CHANNELS, ctr_vals, color=ch_clrs, height=0.55, alpha=0.9)
    for i,v in enumerate(ctr_vals):
        ax3.text(v+0.05, i, f"{v:.1f}%", va="center", fontsize=9, color=WHITE)
    ax3.set_title("CTR Promedio por Canal",color=WHITE,fontsize=12,pad=8,loc="left")
    ax3.set_xlabel("CTR (%)",color=MUTED,fontsize=9)
    ax3.tick_params(colors=MUTED,labelsize=9)
    for sp in ["top","right"]: ax3.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax3.spines[sp].set_color(BORDER)
    ax3.grid(axis="x",color=BORDER,alpha=0.5)

    # Conversiones por canal (donut)
    ax4 = fig.add_subplot(gs[2,2])
    ax4.set_facecolor(PANEL)
    conv = [1240, 890, 650, 420]
    ax4.pie(conv, labels=CHANNELS, colors=ch_clrs, autopct="%1.0f%%",
            startangle=90, wedgeprops={"linewidth":2,"edgecolor":BG},
            textprops={"color":WHITE,"fontsize":8.5})
    ax4.set_title("Conversiones por Canal",color=WHITE,fontsize=11,pad=6)

    # Radar de performance (simulado como barras agrupadas)
    ax5 = fig.add_subplot(gs[2,3])
    ax5.set_facecolor(PANEL)
    metrics_radar = ["ROAS","CTR","CVR","CPA opt."]
    scores = [85, 72, 68, 91]
    bar_c2 = [GREEN if s>=80 else ORANGE if s>=65 else RED for s in scores]
    ax5.bar(metrics_radar, scores, color=bar_c2, width=0.55, alpha=0.9)
    ax5.axhline(70,color=WHITE,linestyle="--",alpha=0.3,linewidth=1)
    ax5.set_ylim(0,110)
    ax5.set_title("Score de Campana (/100)",color=WHITE,fontsize=10,pad=8,loc="left")
    ax5.tick_params(colors=MUTED,labelsize=8.5)
    for sp in ["top","right"]: ax5.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax5.spines[sp].set_color(BORDER)
    for i,(m,s) in enumerate(zip(metrics_radar,scores)):
        ax5.text(i, s+1.5, str(s), ha="center", fontsize=9, color=WHITE, fontweight="bold")

    # Tendencia semanal de ROAS
    ax6 = fig.add_subplot(gs[3,:3])
    ax6.set_facecolor(PANEL)
    weeks = [f"Sem {i+1}" for i in range(8)]
    for ci, (client, base_roas) in enumerate(zip(CLIENTS, ROAS)):
        series = np.clip(np.array([base_roas]*8) + np.random.normal(0, 0.25, 8), 1.5, 7.0)
        lc     = [BLUE,GREEN,ORANGE,GOLD,PURPLE][ci]
        ax6.plot(weeks, series, color=lc, linewidth=2, marker="o", markersize=4, label=client)
    ax6.axhline(3.5, color=WHITE, linestyle="--", alpha=0.3, linewidth=1.2)
    ax6.set_title("Evolucion Semanal de ROAS por Cliente",color=WHITE,fontsize=12,pad=8,loc="left")
    ax6.set_ylabel("ROAS",color=MUTED,fontsize=9)
    ax6.tick_params(colors=MUTED,labelsize=9)
    for sp in ["top","right"]: ax6.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax6.spines[sp].set_color(BORDER)
    ax6.legend(fontsize=8,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL,loc="upper right")
    ax6.grid(axis="y",color=BORDER,alpha=0.4)

    # Insight
    ax7 = fig.add_subplot(gs[3,3])
    ax7.set_facecolor(PANEL)
    for sp in ax7.spines.values(): sp.set_edgecolor(GOLD); sp.set_linewidth(2)
    ax7.set_xticks([]); ax7.set_yticks([])
    ax7.text(0.5,0.5,
             "INSIGHT\n\n"
             "LuxHome ROAS\n"
             "5.3x — reasignar\n"
             "presupuesto de\n"
             "FitLife (2.8x)\n"
             "hacia sus canales\n"
             "top performers.",
             ha="center",va="center",fontsize=8.5,color=WHITE,
             transform=ax7.transAxes,linespacing=1.7)

    plt.savefig(path,dpi=150,bbox_inches="tight",facecolor=BG,edgecolor="none")
    plt.close()
    print(f"Dashboard guardado: {path}")

if __name__=="__main__":
    generate(os.path.join(OUT,"dashboard_p4_marketing.png"))
