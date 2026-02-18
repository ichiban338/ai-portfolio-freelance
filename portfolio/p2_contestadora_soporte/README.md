# Proyecto 2 – Contestadora AI Automatizada para Soporte Tecnico

> **TechSolve** · Sector Tecnologia B2B · Primera linea de soporte automatizada

---

## Que hace este proyecto?

Sistema de contestadora inteligente que gestiona llamadas y SMS de soporte tecnico de forma
autonoma. Clasifica la intencion del cliente, resuelve casos comunes con la base de conocimiento
tecnico y deriva los casos complejos al agente con contexto completo.

---

## Metricas (simuladas)

| KPI | Valor |
|-----|-------|
| Llamadas gestionadas/mes | 720 |
| Resolucion automatica | 68% |
| Duracion promedio | 3.2 min |
| Reduccion costo operativo | 44% |
| Disponibilidad sistema | 99.7% |

---

## Estructura del proyecto

```
p2_contestadora_soporte/
├── config/
│   └── settings.py          # Twilio + API keys + parametros
├── src/
│   ├── voice_operator.py    # Motor AI de contestadora
│   ├── twilio_webhooks.py   # Endpoints TwiML para llamadas
│   └── generate_dashboard.py
├── outputs/
├── demo.py
├── requirements.txt
└── README.md
```

---

## Instalacion y ejecucion

```bash
# Instalar dependencias
pip install -r requirements.txt

# (Opcional) configurar credenciales
export ANTHROPIC_API_KEY="sk-ant-..."
export TWILIO_ACCOUNT_SID="ACxxxxxxx"
export TWILIO_AUTH_TOKEN="your_token"

# Demo en terminal (sin Twilio)
python demo.py

# Generar dashboard
python src/generate_dashboard.py

# Levantar servidor para webhooks de Twilio
python src/twilio_webhooks.py
# Exponer con: ngrok http 5001
# Configurar webhook en Twilio: https://tu-url.ngrok.io/voice/incoming
```

---

## Flujo de una llamada

```
Llamada entrante
      |
  Twilio IVR
      |
  Menu de opciones (1=password, 2=conexion, 3=facturacion, 0=agente)
      |
  VoiceOperator.process()  →  Claude API
      |
  ¿Resuelto?
  SI → Confirmar + SMS de resumen
  NO → Transferir con contexto al agente
```

---

## Endpoints (Twilio Webhooks)

| Ruta | Descripcion |
|------|-------------|
| POST `/voice/incoming` | Llamada entrante → menu IVR |
| POST `/voice/menu` | Procesamiento de seleccion |
| POST `/voice/followup` | Confirmacion de resolucion |
| POST `/sms/incoming` | SMS entrante con respuesta AI |
| GET `/dashboard` | Metricas en JSON |

---

## Dependencias

```
anthropic>=0.30.0
flask>=3.0.0
twilio>=8.0.0
python-dotenv>=1.0.0
```
