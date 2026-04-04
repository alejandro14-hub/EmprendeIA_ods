# AI Log - Equipo EmprendeIA_ods

## Herramientas
- Antigravity (Agente Codificador LLM)

## Filosofía de uso
Decidimos usar IA exclusivamente como un acelerador técnico para la materialización visual y la estructuración del front-end. Toda la investigación sociológica, la selección de variables cruzadas (Pobreza → Abandono → Desempleo), la identificación estadística del bache de datos de la ENOE 2020 y la narrativa principal fueron decisiones intelectuales 100% del núcleo del equipo. Nuestro criterio: si atañe al conocimiento del contexto socioeconómico mexicano, lo decide y analiza el humano; si atañe a sintaxis de HTML/CSS y librerías de graficación, se delega y revisa.

## Registro de uso 

### 2026-04-03 | Antigravity | Refactorización de Dashboard a Arquitectura Multi-Página
- *Tarea*: Solicitamos al agente que transicionara nuestro dashboard `.qmd` originario (basado en matplotlib estático) a un formato dinámico sin que las gráficas se ocultaran o solaparan por falta de espacio web.
- *Prompt*: Transmitiendo la idea conceptual de que "la información está encimada de las gráficas", le pedimos estructurar un tablero que cuente la historia como un portal de periodismo.
- *Resultado*: Nos proveyó una arquitectura de componentes usando `# Page` en Quarto y `.sidebar` dedicado para lograr un efecto expansivo de 70% de lienzo para gráficas y 30% contexto.
- *Decisión*: Adoptamos la estructura propuesta porque permite separar narrativamente las 3 Fases del ciclo de precariedad de manera muy limpia y nos brinda el espacio suficiente para argumentar la transición sociológica.

### 2026-04-03 | Antigravity | Diseño Estético y UI (Dark Mode)
- *Tarea*: Creación de un SCSS personalizado para darle un acabado "premium" y moderno al reporte interactivo.
- *Resultado*: Generación del archivo `modern.scss` adaptando una paleta sombría e implementando la fuente tipográfica Inter.
- *Decisión*: Aceptamos y ajustamos las variables de color. La decisión de usar un "Dark Mode" para periodismo de datos nos pareció ideal dado el tono trágico del abandono escolar (ODS 4) hacia trabajos elementales (ODS 8). Modificamos los tintes sugeridos para estandarizarnos a los colores oficiales de la ONU de cada ODS (Ej: Rojo para ODS 1, Verde oscuro para ODS 8).

### 2026-04-03 | Antigravity | Migración Tridimensional Asistida (Plotly y PyDeck)
- *Tarea*: Le proporcionamos nuestros `DataFrames` pre-limpiados y la lógica condicional que diseñamos manualmente. Pedimos que tradujera nuestros mapas estáticos de Matplotlib a PyDeck tridimensional interactivo, y a un Plotly 3D el cubo de la precariedad.
- *Resultado*: Generación de sintaxis para `px.scatter_3d` y `pdk.Deck` preservando escrupulosamente los apuntadores de datos a nuestros DataFrames originales.
- *Decisión*: Validamos exhaustivamente las variables cruzadas del Cubo. De hecho, el equipo había descubierto previamente que los datos de la ENOE 2020 de INEGI tenían valores nulos (NaN) para la desocupación estatal. Nosotros, como equipo de datos, tomamos la decisión técnica rigurosa de limitar el ODS 8 al año 2019 para mantener la integridad relacional del cubo 3D. La IA no participó en esa limpieza estadística, sólo en el envoltorio gráfico. Del mismo modo, estandarizamos y depuramos manualmente los sufijos numéricos de "Estados Unidos Mexicanos" en los archivos de la SEP (ODS 4).

### 2026-04-03 | Antigravity | Depuración de Caché HTML y Compatibilidad Plotly
- *Tarea*: El renderizador del Quarto Dashboard fallaba e inyectaba tres copias sobrepuestas de la gráfica 3D en el HTML. Le pasamos a la IA la descripción visual del error asumiendo que era nuestro `px.scatter_3d()`.
- *Resultado*: El agente identificó a través de búsqueda web que la versión `Plotly 6.6.0` tenía un *bug oficial general* de incompatibilidad de inyección CSS/HTML con Quarto.
- *Decisión*: Autorizamos al agente hacer un downgrade del motor de graficación en nuestro entorno (`uv add plotly==5.24.1`). Esta decisión técnica nos pareció contundente y ahorró tiempos de depuración infraestructurales, permitiéndonos seguir enfocados en la curaduría narrativa del tablero final.

### NO usamos IA para hacer lo siguiente:
- **La selección teórica de las 3 variables socioeconómicas y los Datasets del origen** (Extracción manual de CONEVAL, SEP e INEGI).
- **El cruce estructural de los datos**: La hipótesis inicial de que "ningún estado tiene mucho abandono escolar sin tener también forzosamente pobreza a la vez" fue concebida y confirmada analíticamente por el equipo.
- **La redacción final del Storytelling:** Las líneas discursivas de los "Actos", y el concepto dramático de *Estudiar No Es Suficiente*, es total redacción y análisis existencial del talento del equipo.
