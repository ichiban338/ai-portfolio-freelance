# Proyecto 3 – Dashboard KPI Ventas para Retailer

> **MegaMart** · Cadena de 12 Sucursales · Visualizacion estrategica de ventas

---

## Que hace este proyecto?

Dashboard interactivo que centraliza ventas, tendencias por categoria, rendimiento
por sucursal, alertas de stock y metricas de clientes. Sustituye reportes manuales
en Excel dispersos por una vista ejecutiva unificada.

---

## Metricas destacadas (simuladas)

| KPI | Valor |
|-----|-------|
| Ventas totales del mes | $2.84M |
| Variacion vs mes anterior | +9.3% |
| Sucursal lider | Norte Centro |
| Productos en riesgo de stock | 8 |
| Tiempo ahorrado en reportes | 8 hrs/semana |
| Tasa de conversion promedio | 7.2% |

---

## Estructura

```
p3_dashboard_ventas/
├── config/
│   └── settings.py
├── src/
│   ├── data_generator.py    # Dataset de ventas simuladas (12 suc, 6 meses)
│   ├── kpi_calculator.py    # Calculo de KPIs y metricas
│   ├── sales_dashboard.py   # Dashboard visual completo
│   └── excel_report.py      # Exportacion a Excel multi-hoja
├── outputs/
├── demo.py
├── requirements.txt
└── README.md
```

---

## Ejecucion

```bash
# Generar dataset + dashboard + Excel en un paso
python demo.py

# Solo el dashboard visual
python src/sales_dashboard.py

# Solo reporte Excel
python src/excel_report.py
```

Salida esperada en `outputs/`:
```
outputs/
├── dashboard_p3_ventas.png     # Dashboard visual 22x14"
└── reporte_megamart.xlsx       # Reporte ejecutivo multi-hoja
```

---

## Como conectar datos reales

1. Reemplaza `src/data_generator.py` con tu fuente de datos:
   - CSV: `pd.read_csv("ventas.csv")`
   - Base de datos: `pd.read_sql(query, engine)`
   - Google Sheets: via `gspread` + `pandas`
2. Ajusta los nombres de columnas en `kpi_calculator.py`
3. El dashboard se regenera automaticamente con datos reales

---

## Dependencias

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
openpyxl>=3.1.0
```
