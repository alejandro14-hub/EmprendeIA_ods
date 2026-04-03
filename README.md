# EmprendeIA_ods 

## Estudiar No Es Suficiente
### La desconexión entre pobreza, educación y empleo digno en México

---

## Equipo

| Nombre | Descripción |
|--------|-------------|
| Alejandro Valentin Saldaña Mendez | Analisis de datos - Visualizacion |
| Eduardo Francisco Peñaloza Uribe  | Narrativa - Storytelling          |
| Tetsu Nicolas Osnaya Quevedo      | Desarrollo - Dashboard           | 



---

## ODS elegidos

| ODS | Nombre | Relación con el proyecto |
|-----|--------|--------------------------|
| **ODS 1** | Sin Pobreza | La pobreza como barrera de entrada al sistema educativo |
| **ODS 4** | Educación de Calidad | La deserción escolar como eslabón perdido |
| **ODS 8** | Trabajo Decente y Crecimiento Económico | La informalidad como destino de quienes no completan su educación |

---

## Pregunta central

> **¿Por qué en México estudiar más años no garantiza salir de la pobreza ni acceder a un empleo formal?**

Esta pregunta guía todo el tablero: exploramos si la relación Pobreza → Educación → Empleo
funciona como se espera, o si hay una desconexión estructural que perpetúa el ciclo.

---

## Estructura del repositorio
```
EmprendeIA_ods/
├── datos/
│   ├── ods1/    ← Datos CONEVAL de pobreza por estado
│   ├── ods4/    ← Datos SEP/INEGI de educación
│   └── ods8/    ← Datos INEGI ENOE de empleo e informalidad
├── scripts/     ← Scripts de limpieza y procesamiento
├── dashboard/   ← Archivos del tablero final
├── LICENSE
├── DECLARATORIA_IA.md
└── EmprendeIA_ODS_Storytelling.ipynb
```

---

## Metadatos de los datos

### ODS 1 — Pobreza

| Dataset | Fuente | Fecha descarga | Licencia | Variables clave |
|---------|--------|---------------|----------|-----------------|
| `Concentrado_indicadores_de_pobreza_2020.xlsx` | CONEVAL | Abril 2026 | Uso libre con atribución | % pobreza, % pobreza extrema por estado (2010, 2015, 2020) |
| `Líneas_de_Pobreza_por_Ingresos_mar2025.xlsx` | CONEVAL | Abril 2026 | Uso libre con atribución | Canasta básica mensual rural/urbano 1992–2025 |
| `1_1_1_a_sh_es.csv` | INEGI / Agenda 2030 | Abril 2026 | Datos abiertos | % población bajo $1.90 USD diarios por estado |
| `1_1_1_dc_637_es.csv` | INEGI / Agenda 2030 | Abril 2026 | Datos abiertos | Pobreza extrema total/urbano/rural 2018–2020 |

### ODS 4 — Educación

| Dataset | Fuente | Fecha descarga | Licencia | Variables clave |
|---------|--------|---------------|----------|-----------------|
| `Educacion_11.xlsx` | SEP / INEGI | Abril 2026 | Datos abiertos | Tasa de abandono escolar por nivel y estado 2000–2024 |
| `Educacion_05.xlsx` | INEGI | Abril 2026 | Datos abiertos | Grado promedio de escolaridad por estado y sexo 2010–2020 |
| `4_1_2_dc_1823_es.csv` | INEGI / Agenda 2030 | Abril 2026 | Datos abiertos | Índice de finalización primaria/secundaria/prepa por estado |
| `Educacion_03.xlsx` | INEGI | Abril 2026 | Datos abiertos | Asistencia escolar por estado 2020 |

### ODS 8 — Empleo

| Dataset | Fuente | Fecha descarga | Licencia | Variables clave |
|---------|--------|---------------|----------|-----------------|
| `8_5_1c_sh_es.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Ingreso medio por hora por tipo de ocupación 2016–2024 |
| `8_5_2_2__sh_es.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Tasa de desocupación por estado, sexo y edad 1995–2020 |
| `Tabulado.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Tasa de informalidad trimestral 2022–2025 |
| `Tabulado__1_.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Tasa de desocupación mensual por sexo 2024–2026 |

---

## Fuentes oficiales

- CONEVAL: https://www.coneval.org.mx
- INEGI ENOE: https://www.inegi.org.mx/programas/enoe/15ymas/
- SEP: https://www.sep.gob.mx
- Agenda 2030 México: https://agenda2030.mx
- ONU ODS: https://unstats.un.org/sdgs/

---

## Cómo ejecutar
```bash
# Requiere uv + miniconda
uv run jupyter notebook EmprendeIA_ODS_Storytelling.ipynb
```

Dependencias: `pandas`, `plotly`, `openpyxl`
