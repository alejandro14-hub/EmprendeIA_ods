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

### Coherencia Narrativa (Módulo C2)
El relato de nuestro tablero está dividido en 3 Actos:
1. **Topografía de la Pobreza:** Condiciona estadísticamente la línea de salida (ODS 1).
2. **Abandono Escolar:** Cómo la falta de ingresos obliga a la deserción media superior (ODS 4).
3. **Condena Laboral:** Cómo los que abandonaron la prepa son absorbidos por ocupaciones elementales sin salarios justos ni formalidad (ODS 8).

### Potencial de Impacto (Módulo C3)
Este tablero expone visual y analíticamente el mito de la "meritocracia pura". Al demostrar tridimensionalmente que la deserción y la pobreza extrema están co-relacionadas, el tablero funciona como una herramienta de divulgación social para crear conciencia en formuladores de políticas públicas sobre por qué las becas escolares por sí solas no solucionan el ciclo sin atacar la pobreza estructural.

---

## Justificación de la Selección de Datos (Módulo B3)
Elegimos la ENOE y el CONEVAL porque son las **únicas fuentes estadísticamente fiables** de cobertura nacional estandarizada.
*   Decidimos enfocar los datos del **ODS 4 en Abandono en Nivel Medio Superior** porque, de acuerdo a la SEP, es el principal embudo formativo donde los jóvenes ingresan a la Población Económicamente Activa.
*   Optamos por aislar los datos del **ODS 8 al año 2019** debido a que los registros de 2020 en adelante presentaban colapsos estadísticos (`NaN`) en la captura de desocupación a causa de la paralización laboral por COVID-19, asegurando así la integridad del modelo tridimensional.

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
├── ai-log.md    ← Registro estratégico de uso de IA
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

## Cómo ejecutar la plataforma

El proyecto ha evolucionado a una aplicación interactiva multi-página desarrollada con **Quarto Dashboards**.

```bash
# Entorno gestionado mediante uv
uv run quarto preview Tablero_ods_EmprendeIA.qmd
```

Dependencias principales instaladas en el contenedor: `pandas`, `plotly`, `pydeck`, `quarto-cli`, `openpyxl`
