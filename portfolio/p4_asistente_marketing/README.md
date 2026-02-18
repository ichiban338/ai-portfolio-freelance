# Proyecto 4 – Asistente AI con Reportes para Agencia de Marketing

> **DigitalPulse Agency** · 5 Clientes Activos · Automatizacion de reportes y atencion

---

## Que hace este proyecto?

Combina un asistente conversacional con generacion automatica de reportes de campanas.
Clientes y account managers consultan metricas en lenguaje natural y reciben reportes
ejecutivos generados por IA sin intervenir manualmente.

---

## Metricas (simuladas)

| KPI | Valor |
|-----|-------|
| Consultas gestionadas/mes | 340 |
| Reportes generados auto | 35/mes |
| Tiempo ahorrado | 9.5 hrs/semana |
| CSAT con asistente | 4.6/5.0 |
| ROAS promedio cartera | 3.8x |

---

## Estructura

```
p4_asistente_marketing/
├── config/
│   └── settings.py
├── src/
│   ├── marketing_assistant.py  # Asistente AI con acceso a metricas
│   ├── report_generator.py     # Generacion automatica de reportes AI
│   ├── campaign_dashboard.py   # Dashboard visual de campanas
│   └── data_simulator.py       # Datos simulados de campanas
├── outputs/
├── demo.py
├── requirements.txt
└── README.md
```

---

## Ejecucion

```bash
# Configurar (opcional)
export ANTHROPIC_API_KEY="sk-ant-..."

# Demo completo: asistente + reporte + dashboard
python demo.py

# Solo dashboard
python src/campaign_dashboard.py
```

---

## Ejemplo de interaccion

```
Account Manager: ¿Como va el ROAS de FreshMart este mes?

NOVA: FreshMart tiene un ROAS global de 3.2x este mes con $8,500 invertidos
y $27,200 generados. Su mejor canal es Google Ads (ROAS 3.8x) y el que necesita
atencion es TikTok (ROAS 2.1x, por debajo del benchmark de 2.5x).
¿Deseas que genere el reporte completo de optimizacion?
```

---

## Dependencias

```
anthropic>=0.30.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
flask>=3.0.0
```
