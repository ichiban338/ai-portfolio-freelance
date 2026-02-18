# ============================================================
# src/knowledge_base.py – Base de conocimiento de TrendStore
# ============================================================

STORE_KNOWLEDGE = {
    "shipping": {
        "standard": "5–7 días hábiles, costo $4.99",
        "express":  "2–3 días hábiles, costo $12.99",
        "free_threshold": "Envío gratis en compras mayores a $75",
        "international": "Disponible a 12 países, 10–15 días hábiles"
    },
    "returns": {
        "window":    "30 días desde la fecha de entrega",
        "condition": "Producto sin uso, con etiquetas originales",
        "process":   "Cuenta → Mis Pedidos → Solicitar Devolución → Imprimir etiqueta",
        "refund_time": "3–5 días hábiles una vez recibido el artículo"
    },
    "products": {
        "categories": ["Ropa", "Calzado", "Accesorios", "Deportivo"],
        "sizes":       "XS a 3XL según producto; consultar tabla de tallas en cada ficha",
        "stock_check": "Disponibilidad en tiempo real en la página de cada producto",
        "new_arrivals": "Colección nueva cada primer lunes del mes"
    },
    "orders": {
        "tracking":      "Número de seguimiento enviado por email al despachar",
        "cancellation":  "Posible hasta 2 horas después de confirmar el pedido",
        "invoice":       "Disponible en Mi Cuenta → Mis Pedidos → Descargar Factura",
        "modification":  "No es posible modificar pedidos ya confirmados"
    },
    "payments": {
        "methods":    "Tarjeta de crédito/débito, PayPal, transferencia bancaria",
        "security":   "Pagos cifrados con SSL/TLS; no almacenamos datos de tarjeta",
        "promotions": "Descuentos activos visibles en la sección de Ofertas"
    }
}

# Intents reconocidos con ejemplos de frases
INTENT_EXAMPLES = {
    "shipping_info":   ["¿cuánto tarda el envío?", "¿cuál es el costo de envío?", "envío gratis"],
    "return_policy":   ["quiero devolver", "política de devolución", "cambio de producto"],
    "order_tracking":  ["dónde está mi pedido", "número de seguimiento", "estado de mi orden"],
    "product_inquiry": ["¿tienen tallas grandes?", "nueva colección", "disponibilidad"],
    "payment_help":    ["métodos de pago", "¿aceptan PayPal?", "pago seguro"],
    "human_escalation":["hablar con un agente", "quiero un humano", "problema con mi cuenta"]
}
