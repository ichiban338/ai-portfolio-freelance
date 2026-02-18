# 🛍️ Proyecto 1 – Chatbot FAQ Inteligente para E-Commerce

> **TrendStore** · Sector Retail Online · Automatización de Atención al Cliente

---

## ¿Qué hace este proyecto?

Chatbot conversacional que responde preguntas frecuentes de clientes (envíos, devoluciones,
pedidos, productos, pagos) de forma inmediata y disponible 24/7. Integrado con Claude API
para comprensión de lenguaje natural y desplegable en cualquier web o plataforma de mensajería.

---

## Métricas del proyecto (simuladas)

| KPI | Valor |
|-----|-------|
| Consultas gestionadas/mes | 1,240 |
| Tasa de resolución autónoma | 74% |
| Tiempo de respuesta promedio | 2.1 seg |
| CSAT | 4.4 / 5.0 |
| Reducción carga de soporte | 61% |

---

## Estructura del proyecto

```
p1_chatbot_faq/
├── config/
│   └── settings.py          # Variables de entorno y configuración
├── src/
│   ├── knowledge_base.py    # Base de conocimiento de la tienda
│   ├── chatbot_engine.py    # Motor conversacional (Claude API)
│   └── api.py               # Servidor Flask con endpoints REST
├── outputs/                 # Dashboards y reportes generados
├── docs/                    # Documentación adicional
├── demo.py                  # 🚀 Demo interactivo en terminal
├── requirements.txt
└── README.md
```

---

## Instalación y ejecución rápida

### 1. Clonar e instalar dependencias
```bash
git clone <repo>
cd p1_chatbot_faq
pip install -r requirements.txt
```

### 2. Configurar API key (opcional para demo)
```bash
# Linux/Mac
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows
set ANTHROPIC_API_KEY=sk-ant-...
```
> **Sin API key**: el proyecto corre en modo demo con respuestas simuladas.

### 3. Ejecutar demo en terminal
```bash
python demo.py
```
Salida esperada:
```
═══════════════════════════════════════
  🛍️  SOFIA – Asistente Virtual TrendStore
  Chatbot FAQ Inteligente | Demo Interactivo
═══════════════════════════════════════
Modo (auto/manual) [auto]: auto

👤 Cliente: ¿Cuánto tarda el envío estándar?
🤖 Sofia:   ¡Hola! El envío estándar tarda 5–7 días hábiles...
```

### 4. Levantar servidor API (requiere API key)
```bash
python src/api.py
# Servidor en http://localhost:5000
```

### 5. Probar endpoint
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "test-001", "message": "¿cuánto tarda el envío?"}'
```

---

## Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/chat` | Enviar mensaje al bot |
| GET | `/metrics` | Métricas de sesión |
| GET | `/health` | Estado del servidor |

---

## Tecnologías utilizadas

- **Python 3.10+**
- **Anthropic Claude API** (`claude-opus-4-6`)
- **Flask** – servidor web ligero
- **JSON** – base de conocimiento estructurada

---

## Cómo funciona (flujo)

```
Usuario → POST /chat → ChatBotEngine → Claude API
                                     ↓
                              Base de conocimiento
                                     ↓
                       Respuesta JSON ← Bot
```

---

## Variables de entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Clave de API de Anthropic | _(demo mode)_ |
| `PORT` | Puerto del servidor | `5000` |
| `DEBUG` | Modo debug Flask | `False` |

---

## Personalización para tu negocio

1. Editar `src/knowledge_base.py` con la información de tu empresa
2. Cambiar `BOT_NAME` y `STORE_NAME` en `config/settings.py`
3. Ajustar el `_system_prompt()` en `chatbot_engine.py` con tu tono de marca
4. Integrar `src/api.py` con tu CRM o plataforma de chat preferida

---

*Proyecto desarrollado como parte del portafolio de IA para freelancers.*
*Métricas presentadas son simuladas con fines demostrativos.*
