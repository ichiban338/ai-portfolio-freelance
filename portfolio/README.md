# 🤖 Portafolio de Inteligencia Artificial — Juan Esteban Agudelo

**Freelancer especializado en soluciones de IA aplicadas a negocios reales.**
Automatizo procesos, construyo chatbots inteligentes y convierto datos en decisiones
con dashboards ejecutivos — usando Python, Claude API y las herramientas correctas para cada problema.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Juan%20Esteban%20Agudelo-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/juan-esteban-agudelo-alonso/)

---

## 🛠️ Servicios

| Servicio | Descripcion |
|----------|-------------|
| 💬 Chatbots y Asistentes AI | Bots conversacionales con Claude/GPT para atencion al cliente, soporte y ventas |
| ⚙️ Automatizacion de Procesos | Flujos automaticos que eliminan tareas repetitivas y reducen errores operativos |
| 📊 Dashboards y Analisis de Datos | Paneles ejecutivos interactivos que transforman datos en decisiones estrategicas |

---

## 📁 Proyectos

### 01 · Chatbot FAQ Inteligente — TrendStore (E-Commerce)

> Chatbot que automatiza respuestas a preguntas frecuentes de clientes con disponibilidad 24/7.

**El problema:** una tienda online recibía +400 consultas semanales sobre envíos, devoluciones y
pedidos. El equipo de soporte tardaba hasta 6 horas en responder, generando abandono de carritos.

**La solución:** chatbot con Claude API entrenado en la base de conocimiento de la tienda, integrado
en la web, que responde en 2 segundos y escala solo los casos complejos al equipo humano.

**Stack:** `Python` `Claude API` `Flask` `JSON`

| Metrica | Resultado |
|---------|-----------|
| Consultas gestionadas/mes | 1,240 |
| Resolucion automatica | 74% |
| Tiempo de respuesta | 2.1 seg |
| CSAT | 4.4 / 5.0 |
| Reduccion carga de soporte | 61% |

![Dashboard Chatbot FAQ](portfolio/p1_chatbot_faq/outputs/dashboard_p1_chatbot.png)

---

### 02 · Contestadora AI Automatizada — TechSolve (Soporte Tecnico B2B)

> Sistema de atencion automatica por voz y SMS para primera linea de soporte tecnico.

**El problema:** empresa de software con 500 clientes activos recibía 180 llamadas semanales.
El 40% fuera de horario quedaban sin respuesta, impactando la retención de clientes.

**La solución:** contestadora inteligente con Twilio + Claude API que clasifica la consulta,
resuelve casos comunes paso a paso y transfiere casos complejos con contexto completo al agente.

**Stack:** `Python` `Claude API` `Twilio` `Flask`

| Metrica | Resultado |
|---------|-----------|
| Llamadas gestionadas/mes | 720 |
| Resolucion automatica | 68% |
| Duracion promedio | 3.2 min |
| Disponibilidad | 99.7% |
| Reduccion costo operativo | 44% |

![Dashboard Contestadora](portfolio/p2_contestadora_soporte/outputs/dashboard_p2_contestadora.png)

---

### 03 · Dashboard KPI Ventas — MegaMart (Retail 12 Sucursales)

> Panel ejecutivo que centraliza ventas, tendencias, rendimiento por sucursal y alertas de stock.

**El problema:** cadena de 12 tiendas gestionaba reportes en hojas de calculo separadas.
Los gerentes tardaban 2 dias en consolidar datos y tomaban decisiones con informacion desactualizada.

**La solución:** dashboard interactivo generado automaticamente con Python + Pandas que muestra
KPIs en tiempo real, detecta quiebres de stock antes de que ocurran y elimina reportes manuales.

**Stack:** `Python` `Pandas` `Matplotlib` `openpyxl`

| Metrica | Resultado |
|---------|-----------|
| Sucursales monitoreadas | 12 |
| Tiempo ahorrado en reportes | 8 hrs/semana |
| Productos con alerta de stock | Deteccion automatica |
| Tasa de conversion promedio | 7.2% |

![Dashboard KPI Ventas](portfolio/p3_dashboard_ventas/outputs/dashboard_p3_ventas.png)

---

### 04 · Asistente AI con Reportes — DigitalPulse (Agencia de Marketing)

> Asistente conversacional que consulta metricas de campanas y genera reportes ejecutivos con IA.

**El problema:** agencia con 35 clientes invertia 12 horas semanales consolidando metricas de
Meta, Google Ads y email marketing para armar reportes manuales.

**La solución:** asistente que responde en lenguaje natural sobre el estado de cualquier campana
y genera reportes ejecutivos automaticamente con insights y recomendaciones estrategicas.

**Stack:** `Python` `Claude API` `Pandas` `Matplotlib`

| Metrica | Resultado |
|---------|-----------|
| Consultas gestionadas/mes | 340 |
| Reportes generados automaticamente | 35 / mes |
| Tiempo ahorrado | 9.5 hrs/semana |
| ROAS promedio cartera | 4.2x |
| CSAT asistente | 4.6 / 5.0 |

![Dashboard Marketing](portfolio/p4_asistente_marketing/outputs/dashboard_p4_marketing.png)

---

### 05 · Contestadora Inteligente + Analisis — ContactPro (Call Center)

> Sistema que automatiza la atencion y convierte cada llamada en datos estrategicos accionables.

**El problema:** call center con 48 agentes sin visibilidad sobre que temas generaban mas llamadas,
en que horarios se saturaba el sistema, ni que porcentaje podia resolverse automaticamente.

**La solución:** contestadora AI que clasifica y resuelve consultas automaticamente, registra
cada interaccion como dato estructurado y genera dashboards + reportes de insights para optimizar
operaciones y distribucion de agentes.

**Stack:** `Python` `Claude API` `Pandas` `Twilio` `Matplotlib`

| Metrica | Resultado |
|---------|-----------|
| Interacciones analizadas | 3,200 / mes |
| Resolucion automatica | 62% |
| Reduccion tiempo de espera | 38% |
| Ahorro operativo estimado | $4,200 / mes |
| Payback estimado | < 2 meses |

![Dashboard Call Center](portfolio/p5_callcenter_analytics/outputs/dashboard_p5_callcenter.png)

---

## 🚀 Como ejecutar los proyectos

```bash
# 1. Clonar el repositorio
git clone https://github.com/ichiban338/ai-portfolio-freelance.git
cd ai-portfolio-freelance/portfolio

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. (Opcional) Activar respuestas reales con Claude
set ANTHROPIC_API_KEY=sk-ant-tu-clave-aqui   # Windows
export ANTHROPIC_API_KEY=sk-ant-...           # Mac/Linux

# 4. Generar todos los dashboards de una vez
python generate_all.py

# 5. O correr el demo de un proyecto especifico
python p1_chatbot_faq/demo.py
```

> **Sin API key:** todos los proyectos funcionan en modo demo con respuestas simuladas realistas.

---

## 🧱 Estructura del repositorio

```
ai-portfolio-freelance/
└── portfolio/
    ├── p1_chatbot_faq/
    │   ├── config/
    │   ├── src/
    │   ├── outputs/        <- dashboards PNG
    │   ├── demo.py
    │   └── README.md
    ├── p2_contestadora_soporte/
    ├── p3_dashboard_ventas/
    ├── p4_asistente_marketing/
    ├── p5_callcenter_analytics/
    ├── generate_all.py
    └── requirements.txt
```

---

## 📬 Contacto

¿Tienes un proceso que quieres automatizar o datos que no sabes como aprovechar?

[![LinkedIn](https://img.shields.io/badge/Escribeme%20en-LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/juan-esteban-agudelo-alonso/)

---

*Las metricas presentadas en este portafolio son simuladas con fines demostrativos.
El codigo es funcional y adaptable a datos y sistemas reales de cada cliente.*
