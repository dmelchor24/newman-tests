# Fast API Testing Project

Proyecto de pruebas automatizadas para una API desarrollada con Fast API.

## Estructura del Proyecto

```
.
├── docs/                  # Documentación y reportes HTML
├── postman/              # Colecciones de Postman
├── results/              # Resultados de ejecución de tests
├── scripts/              # Scripts de automatización
│   └── execute-tests.py  # Script principal de ejecución
└── requirements.txt      # Dependencias del proyecto
```

## Requisitos

- Python 3.x
- pip

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecución local

```bash
python scripts/execute-tests.py
```

Con URL personalizada:
```bash
python scripts/execute-tests.py --base-url=https://api.ejemplo.com
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

Los resultados se guardarán en la carpeta `results/` con timestamp.

## CI/CD

El proyecto incluye un workflow de GitHub Actions (`postman-tests.yaml`) que:
- Ejecuta automáticamente los tests en push/PR
- Publica los reportes en GitHub Pages
- Guarda los resultados como artefactos

Para usar GitHub Pages, habilita Pages en la configuración del repositorio usando la rama `gh-pages`.

## Documentación

La documentación HTML se encuentra en la carpeta `docs/`.
