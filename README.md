# Fast API Testing Project

Proyecto de pruebas automatizadas para una API desarrollada con Fast API usando Postman/Newman.

![Newman Tests](https://github.com/dmelchor24/newman-tests/actions/workflows/postman-tests.yaml/badge.svg)

📊 **Reporte de la última ejecución (GitHub Pages)**  
👉 https://dmelchor24.github.io/newman-tests


## Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       └── postman-tests.yaml  # Workflow de GitHub Actions
├── docs/                       # Reportes HTML para GitHub Pages
│   ├── index.html             # Último reporte generado
│   └── .last_run.txt          # Timestamp de última ejecución
├── postman/                   # Colecciones de Postman
│   └── Endpoints Fast API.postman_collection.json
├── results/                   # Historial de resultados por timestamp
│   └── run_YYYYMMDD_HHMMSS/
│       └── report.html
├── scripts/                   # Scripts de automatización
│   └── execute-tests.py       # Script principal de ejecución
├── docker-compose.yml         # Configuración Docker
├── Dockerfile                 # Imagen Docker para tests
└── requirements.txt           # Dependencias Python
```

## Requisitos

- Python 3.x
- Node.js 18+ (para Newman)
- npm

## Instalación

1. Clonar el repositorio

2. Instalar Newman y el reporter:
   ```bash
   npm install -g newman
   npm install -g newman-reporter-htmlextra
   ```

3. (Opcional) Crear un entorno virtual Python:
   ```bash
   python -m venv venv
   ```

4. (Opcional) Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

5. Instalar dependencias Python (si las hay):
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecución local

Por defecto usa `http://localhost:8000`:
```bash
python scripts/execute-tests.py
```

Con URL personalizada (opción 1 - argumento CLI):
```bash
python scripts/execute-tests.py --base-url=https://api.ejemplo.com
```

Con URL personalizada (opción 2 - variable de entorno):
```bash
export BASE_URL=https://api.ejemplo.com  # Linux/Mac
set BASE_URL=https://api.ejemplo.com     # Windows
python scripts/execute-tests.py
```

### Ejecución con Docker

Construir y ejecutar:
```bash
docker-compose up --build
```

Con URL personalizada:
```bash
BASE_URL=https://api.ejemplo.com docker-compose up
```

## Resultados

Los reportes se generan en dos ubicaciones:

1. **Historial**: `results/run_YYYYMMDD_HHMMSS/report.html` - Se mantiene un historial de todas las ejecuciones
2. **GitHub Pages**: `docs/index.html` - Siempre contiene el último reporte generado (incluso si los tests fallan)

## CI/CD con GitHub Actions

El proyecto incluye un workflow (`postman-tests.yaml`) que se ejecuta manualmente desde la pestaña Actions.

### Características:
- Ejecuta los tests contra una URL configurable
- Publica automáticamente los reportes en GitHub Pages (rama `gh-pages`)
- Guarda los resultados como artefactos (disponibles por 30 días)
- Genera reportes incluso cuando los tests fallan

### Configuración de GitHub Pages:

1. Ve a Settings → Pages
2. Selecciona Source: "Deploy from a branch"
3. Selecciona Branch: `gh-pages` y carpeta `/ (root)`
4. Guarda los cambios

### Ejecutar el workflow:

1. Ve a la pestaña "Actions"
2. Selecciona "Postman API Tests"
3. Click en "Run workflow"
4. Ingresa la URL base (o usa la predeterminada)
5. Click en "Run workflow"

## Notas

- El script siempre copia el reporte a `docs/index.html`, incluso si los tests fallan
- Los reportes HTML incluyen detalles completos de cada request/response
- El timestamp de la última ejecución se guarda en `docs/.last_run.txt`
