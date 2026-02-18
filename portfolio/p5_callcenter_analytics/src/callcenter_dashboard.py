#!/usr/bin/env python3
# src/callcenter_dashboard.py – ContactPro Call Center

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta
import random

OUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

BG, PANEL, BORDER = "#060A14","#0C1420","#162030"
BLUE,GREEN,ORANGE,RED,GOLD,PURPLE,TEAL,MUTED,WHITE=(
    "#3B82F6","#10B981","#F59E0B","#EF4444",
    "#FBBF24","#8B5CF6","#06B6D4","#64748B","#F1F5F9"
)

def kpi(ax,title,val,sub,color):
    ax.set_facecolor(PANEL)
    for sp in ax.spines.values(): sp.set_edgecolor(color); sp.set_linewidth(2.5)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5,0.78,title, ha="center",fontsize=9,  color=MUTED, transform=ax.transAxes)
    ax.text(0.5,0.46,val,   ha="center",fontsize=18, color=color, transform=ax.transAxes,fontweight="bold")
    ax.text(0.5,0.17,sub,   ha="center",fontsize=8,  color=MUTED, transform=ax.transAxes)

def make_call_data(n=500):
    random.seed(42); np.random.seed(42)
    hour_w = {8:.04,9:.09,10:.13,11:.12,12:.08,13:.06,
              14:.10,15:.12,16:.11,17:.09,18:.04,19:.02}
    cats = {"billing":.28,"technical":.35,"cancellation":.12,"product_info":.25}
    res_rates = {"billing":.78,"technical":.55,"cancellation":.42,"product_info":.89}
    rows = []
    base = datetime.now()-timedelta(days=60)
    for i in range(n):
        d = base+timedelta(days=random.randint(0,59))
        cat = random.choices(list(cats),weights=list(cats.values()))[0]
        resolved = random.random()<res_rates[cat]
        rows.append({
            "date": d.strftime("%Y-%m-%d"),
            "hour": random.choices(list(hour_w),weights=list(hour_w.values()))[0],
            "category": cat,
            "resolved": resolved,
            "duration": round(random.uniform(1.5,4.5) if resolved else random.uniform(4,9),2),
            "csat": round(min(5,max(1,np.random.normal(4.2 if resolved else 2.7,.5))),1),
            "channel": random.choices(["IVR Voz","SMS","WhatsApp"],weights=[.60,.25,.15])[0]
        })
    return pd.DataFrame(rows)

def generate(path):
    df = make_call_data()

    fig = plt.figure(figsize=(22,14))
    fig.patch.set_facecolor(BG)
    gs  = gridspec.GridSpec(4,4,figure=fig,hspace=0.46,wspace=0.32,
                            top=0.91,bottom=0.05,left=0.04,right=0.97)

    fig.text(0.5,0.965,"ContactPro — Dashboard Operacional de Call Center AI",
             ha="center",fontsize=17,fontweight="bold",color=WHITE)
    fig.text(0.5,0.944,
             f"Periodo: 60 dias  |  {len(df):,} interacciones  |  Disponibilidad: 99.7%  |  {datetime.now().strftime('%d/%b/%Y')}",
             ha="center",fontsize=9,color=MUTED)

    # KPI Cards
    total    = len(df)
    resolved = df["resolved"].sum()
    res_pct  = resolved/total*100
    avg_dur  = df["duration"].mean()
    avg_csat = df["csat"].mean()
    kpi(fig.add_subplot(gs[0,0]),"Total Llamadas",   f"{total:,}",         "En 60 dias",         BLUE)
    kpi(fig.add_subplot(gs[0,1]),"Resolucion Auto",  f"{res_pct:.0f}%",    f"{resolved:,} casos",GREEN)
    kpi(fig.add_subplot(gs[0,2]),"Duracion Media",   f"{avg_dur:.1f} min", "Por interaccion",    ORANGE)
    kpi(fig.add_subplot(gs[0,3]),"CSAT Promedio",    f"{avg_csat:.2f}/5",  "Satisfaccion",       GOLD)

    # Volumen por hora
    ax1 = fig.add_subplot(gs[1,:2])
    ax1.set_facecolor(PANEL)
    hourly = df.groupby("hour").size()
    hours  = hourly.index.tolist()
    vols   = hourly.values
    peak   = hours[np.argmax(vols)]
    bc     = [GREEN if h==peak else "#1A2A3A" for h in hours]
    ax1.bar(hours,vols,color=bc,width=0.7,alpha=0.9)
    ax1.axhline(vols.mean(),color=GOLD,linestyle="--",alpha=0.5,linewidth=1.2,
                label=f"Prom: {vols.mean():.0f}/hr")
    ax1.set_title(f"Volumen por Hora (Pico: {peak}:00 hrs)",
                  color=WHITE,fontsize=12,pad=8,loc="left")
    ax1.set_xlabel("Hora",color=MUTED,fontsize=9)
    ax1.set_ylabel("Llamadas",color=MUTED,fontsize=9)
    ax1.tick_params(colors=MUTED,labelsize=9)
    for sp in ["top","right"]: ax1.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax1.spines[sp].set_color(BORDER)
    ax1.legend(fontsize=8,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL)

    # Resolucion por categoria
    ax2 = fig.add_subplot(gs[1,2:])
    ax2.set_facecolor(PANEL)
    cat_res = df.groupby("category").agg(total=("resolved","count"),
                                          res=("resolved","sum")).reset_index()
    cat_res["pct"] = cat_res["res"]/cat_res["total"]*100
    cat_res["label"] = cat_res["category"].str.replace("_"," ").str.title()
    cat_res = cat_res.sort_values("pct",ascending=False)
    rc = [GREEN if v>=70 else ORANGE if v>=50 else RED for v in cat_res["pct"]]
    bars = ax2.bar(cat_res["label"],cat_res["pct"],color=rc,width=0.55,alpha=0.9)
    ax2.axhline(70,color=WHITE,linestyle="--",alpha=0.3,linewidth=1.2,label="Objetivo 70%")
    ax2.set_ylim(0,110)
    ax2.set_title("Resolucion Automatica por Categoria",
                  color=WHITE,fontsize=12,pad=8,loc="left")
    ax2.set_ylabel("% Resuelto",color=MUTED,fontsize=9)
    ax2.tick_params(colors=MUTED,labelsize=9,axis="x",rotation=12)
    ax2.tick_params(colors=MUTED,labelsize=9,axis="y")
    for sp in ["top","right"]: ax2.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax2.spines[sp].set_color(BORDER)
    ax2.legend(fontsize=8,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL)
    for b,v in zip(bars,cat_res["pct"]):
        ax2.text(b.get_x()+b.get_width()/2,v+1,f"{v:.0f}%",
                 ha="center",fontsize=9.5,color=WHITE,fontweight="bold")

    # CSAT diario
    ax3 = fig.add_subplot(gs[2,:2])
    ax3.set_facecolor(PANEL)
    daily_csat = df.groupby("date")["csat"].mean().reset_index().tail(30)
    ax3.fill_between(range(len(daily_csat)),daily_csat["csat"],alpha=0.2,color=TEAL)
    ax3.plot(range(len(daily_csat)),daily_csat["csat"],color=TEAL,linewidth=2)
    ax3.axhline(4.0,color=GOLD,linestyle="--",alpha=0.5,linewidth=1.2,label="Objetivo 4.0")
    ax3.set_ylim(2,5.5)
    ax3.set_title("CSAT Diario — Ultimos 30 dias",color=WHITE,fontsize=12,pad=8,loc="left")
    ax3.set_ylabel("Puntuacion",color=MUTED,fontsize=9)
    ax3.tick_params(colors=MUTED,labelsize=8.5)
    ax3.set_xticks(range(0,len(daily_csat),5))
    ax3.set_xticklabels([f"D{i+1}" for i in range(0,len(daily_csat),5)],fontsize=8)
    for sp in ["top","right"]: ax3.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax3.spines[sp].set_color(BORDER)
    ax3.legend(fontsize=8,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL)

    # Canal de contacto
    ax4 = fig.add_subplot(gs[2,2])
    ax4.set_facecolor(PANEL)
    ch = df.groupby("channel").size()
    ax4.pie(ch.values,labels=ch.index,colors=[BLUE,GREEN,PURPLE],
            autopct="%1.0f%%",startangle=90,
            wedgeprops={"linewidth":2,"edgecolor":BG},
            textprops={"color":WHITE,"fontsize":9})
    ax4.set_title("Canal de Contacto",color=WHITE,fontsize=11,pad=6)

    # Resolucion vs Escalacion semanal
    ax5 = fig.add_subplot(gs[2,3])
    ax5.set_facecolor(PANEL)
    df["week"] = pd.to_datetime(df["date"]).dt.isocalendar().week
    weekly = df.groupby("week")["resolved"].agg(["sum","count"]).tail(6)
    w_pct  = (weekly["sum"]/weekly["count"]*100).values
    wk_l   = [f"Sem {i+1}" for i in range(len(w_pct))]
    ax5.bar(wk_l,[100]*len(w_pct),color=ORANGE,alpha=0.6,width=0.55,label="Escalado")
    ax5.bar(wk_l,w_pct,color=GREEN,alpha=0.9,width=0.55,label="Resuelto")
    ax5.set_ylim(0,115)
    ax5.set_title("Resolucion Semanal (%)",color=WHITE,fontsize=10,pad=8,loc="left")
    ax5.tick_params(colors=MUTED,labelsize=8.5)
    for sp in ["top","right"]: ax5.spines[sp].set_visible(False)
    for sp in ["bottom","left"]: ax5.spines[sp].set_color(BORDER)
    ax5.legend(fontsize=8,framealpha=0.2,labelcolor=WHITE,facecolor=PANEL)

    # Insights estratégicos (fila 3)
    ax6 = fig.add_subplot(gs[3,:3])
    ax6.set_facecolor("#0A1520")
    for sp in ax6.spines.values(): sp.set_edgecolor(BLUE); sp.set_linewidth(1.5)
    ax6.set_xticks([]); ax6.set_yticks([])

    top_cat  = df.groupby("category").size().idxmax().replace("_"," ").title()
    low_cat  = cat_res.nsmallest(1,"pct")["label"].values[0]
    est_save = int(res_pct/100 * total * 2.1)

    insights = [
        (f"Categoria mas frecuente: {top_cat} (35% de llamadas)",    BLUE),
        (f"Resolucion automatica global: {res_pct:.0f}%",            GREEN),
        (f"Categoria critica: {low_cat} — resolucion bajo 50%",      RED),
        (f"Ahorro estimado: ~${est_save:,} USD / mes",               GOLD),
        (f"Hora pico: {peak}:00 — reforzar disponibilidad",          ORANGE),
        (f"CSAT promedio: {avg_csat:.2f}/5  |  Objetivo: 4.0",       TEAL),
    ]
    ax6.text(0.01,0.92,"INSIGHTS ESTRATEGICOS GENERADOS POR IA",
             va="top",fontsize=11,fontweight="bold",color=WHITE,transform=ax6.transAxes)
    for i,(text,color) in enumerate(insights):
        y = 0.72 - i*0.12
        ax6.add_patch(plt.Rectangle((0.01,y-0.04),0.011,0.07,
                                    facecolor=color,transform=ax6.transAxes))
        ax6.text(0.03,y+0.01,text,va="center",fontsize=9.5,color=WHITE,transform=ax6.transAxes)

    # ROI box
    ax7 = fig.add_subplot(gs[3,3])
    ax7.set_facecolor(PANEL)
    for sp in ax7.spines.values(): sp.set_edgecolor(GREEN); sp.set_linewidth(2)
    ax7.set_xticks([]); ax7.set_yticks([])
    ax7.text(0.5,0.5,
             "ROI ESTIMADO\n\n"
             f"Casos auto:\n"
             f"{resolved:,} de {total:,}\n\n"
             f"Ahorro: ~${est_save:,}\n"
             "por mes\n\n"
             f"Payback:\n< 2 meses",
             ha="center",va="center",fontsize=8.5,color=WHITE,
             transform=ax7.transAxes,linespacing=1.7)

    plt.savefig(path,dpi=150,bbox_inches="tight",facecolor=BG,edgecolor="none")
    plt.close()
    print(f"Dashboard guardado: {path}")

if __name__=="__main__":
    generate(os.path.join(OUT,"dashboard_p5_callcenter.png"))
