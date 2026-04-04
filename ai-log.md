# AI Log - Equipo EmprendeIA_ods

## Herramientas
- ChatGPT / Claude (claude.ai)
- GitHub Copilot / Cursor (Autocompletado de código)

## Filosofía de uso
Decidimos usar IA **exclusivamente para tareas mecánicas** de sintaxis visual (CSS/HTML) y para debuguear errores de compilación (`quarto preview`). La investigación sociológica, el análisis exploratorio con pandas, la selección de parámetros estadísticos y la narrativa del proyecto (Storytelling) son decisiones editoriales e intelectuales 100% del equipo. 

Nuestro criterio rector fue claro: si la decisión atañe al conocimiento de la estructura social de México o a la validez de los datos de INEGI/SEP/CONEVAL, la hacemos nosotros manualmente. Si es sintaxis pura de JavaScript/D3/Plotly, usamos auto-completado y revisamos exhaustivamente la salida técnica para evitar alucinaciones.

## Registro de uso 

### 2026-04-03 | Claude/ChatGPT | Refactorización Visual de Matplotlib a Opciones Interactivas
- *Tarea*: Originalmente armamos nuestras gráficas 3D en Matplotlib estático con nuestros DataFrames depurados. Decidimos migrar a mapas interactivos y le pedimos a la IA la sintaxis base (el "boilerplate") para traducir nuestro código existente a `px.scatter_3d` (Plotly) y `PyDeck`.
- *Resultado*: Nos dio las maquetas de sintaxis de ambas librerías.
- *Decisión y Modificación*: **Nosotros ajustamos todos los hiperparámetros visuales**. Modificamos manualmente los colores, bloqueamos la paleta de tintes para que coincidieran con la identidad gráfica oficial de la ONU e inyectamos expresamente nuestra lógica pre-calculada de "Abandono * Pobreza" para que el mapeo de color (Z-axis) tuviera coherencia demográfica.

### 2026-04-03 | Copilot/Cursor | Maquetación Multi-Página en Quarto
- *Tarea*: Nuestro dashboard presentaba amontonamiento visual. Pedimos sugerencias de sintaxis en `qmd` para hacer un layout limpio ("Dime cómo separar las gráficas en 3 pestañas o páginas independientes en Quarto").
- *Resultado*: Generó la estructura de `# Páginas` y `.sidebar`.
- *Decisión y Modificación*: Nosotros distribuimos el contenido lógicamente. Usamos la estructura técnica de las páginas pero invertimos horas separando los "3 Actos" de nuestra narrativa manual en cada contenedor, dándole total prioridad a nuestro *storytelling* en los paneles laterales. 

### 2026-04-03 | Claude (Depuración) | Bug crítico del Renderizador (Plotly + Quarto)
- *Tarea*: Al hacer render en Quarto, el motor inyectaba tres gráficas repetidas en el frontend. No encontrábamos el error en nuestro código.
- *Resultado*: Le pegamos el *Traceback* de salida y la IA detectó que había un bug oficial documentado en la versión `Plotly 6.6.0` con la inyección de CSS de Quarto.
- *Decisión y Modificación*: Nosotros ejecutamos el *downgrade* técnico seguro de nuestro entorno administrado en uv, bajándolo a la versión estable `plotly==5.24.1` y limpiando archivos en caché (`.quarto_ipynb_`). 

### NO usamos IA para hacer lo siguiente:
- **La selección teórica de variables socioeconómicas y uso de la API/Descarga original** (Exploración propia de CONEVAL, SEP e INEGI).
- **El cruce estructural de los datos**: La hipótesis inicial de que la deserción se correlaciona con la pobreza municipal para derivar en informalidad fue concebida y comprobada por este equipo.
- **La decisión estadística de truncar el ODS 8**: Nosotros notamos la explosión de *NaNs* por el COVID en 2020 dentro de la base de la ENOE y tomamos matemáticamente la decisión de congelar el modelo en 2019 para presentar un modelo correlacional estructural (sin ruido por contingencia sanitaria).
- **La redacción final del Storytelling y las conclusiones trágicas** del "Tercer Acto", así como la selección gráfica.
