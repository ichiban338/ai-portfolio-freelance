# Proyecto 5 – Contestadora Inteligente con Analisis de Datos

> **ContactPro** · Call Center · Automatizacion + Inteligencia de Negocio

---

## Que hace este proyecto?

Automatiza la primera capa de atencion del call center y convierte cada interaccion
en datos estructurados. El sistema clasifica intenciones, resuelve casos automaticamente,
escala con contexto y genera reportes de patrones para optimizar operaciones.

---

## Metricas (simuladas, 60 dias)

| KPI | Valor |
|-----|-------|
| Interacciones analizadas | 500+ |
| Resolucion automatica | 62% |
| Duracion media auto | 2.8 min vs 8.4 min con agente |
| Reduccion tiempo de espera | 38% |
| Ahorro operativo estimado | $4,200/mes |
| CSAT promedio | 3.85/5.0 |

---

## Estructura

```
p5_callcenter_analytics/
├── config/
│   └── settings.py
├── src/
│   ├── intelligent_operator.py  # Motor AI de contestadora + clasificacion
│   ├── data_analyzer.py         # Analisis de patrones de interacciones
│   ├── callcenter_dashboard.py  # Dashboard operacional visual
│   └── insight_reporter.py      # Generacion de reportes AI
├── outputs/
├── demo.py
├── requirements.txt
└── README.md
```

---

## Ejecucion

```bash
# (Opcional) API key para respuestas reales
export ANTHROPIC_API_KEY="sk-ant-..."

# Demo completo
python demo.py

# Solo dashboard con datos simulados
python src/callcenter_dashboard.py
```

---

## Flujo completo del sistema

```
Llamada / SMS entrante
        |
   Clasificacion de intencion (Claude AI)
        |
   ¿Puede resolverse automaticamente?
   SI ──> Respuesta + confirmacion + log
   NO ──> Escalar con contexto al agente
        |
   Registrar en base de datos
        |
   Analisis periodico de patrones (Pandas)
        |
   Dashboard actualizado + Reporte AI
        |
   Recomendaciones operativas
```

---

## Casos de uso demostrados

1. Consulta de facturacion → resuelta automaticamente (88%)
2. Error de conexion → guia paso a paso (55% resolucion)
3. Cancelacion de servicio → retencion + opciones (42%)
4. Informacion de producto → respuesta inmediata (89%)

---

## Dependencias

```
anthropic>=0.30.0
flask>=3.0.0
twilio>=8.0.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
python-dotenv>=1.0.0
```
