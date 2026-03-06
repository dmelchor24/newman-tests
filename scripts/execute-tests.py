import time
import subprocess
import os
import sys
import shutil
import platform

# Creación de timestamp
timestamp = time.strftime("%Y%m%d_%H%M%S")

# Definir directorios
results_dir = f"results/run_{timestamp}"
docs_dir = "docs"

os.makedirs(results_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# BASE_URL por defecto (prioridad: CLI > ENV > default)
base_url = os.getenv("BASE_URL", "https://endpoints-fast-api.onrender.com")

# Leer argumento desde CLI (CI)
for arg in sys.argv:
    if arg.startswith("--base-url="):
        base_url = arg.split("=", 1)[1]

print(f"🌐 Ejecutando pruebas contra: {base_url}")

# Definir rutas de archivos de salida
report_file = f"{results_dir}/report.html"

# Ejecutar Newman
command = [
    "newman", "run",
    "postman/Endpoints Fast API.postman_collection.json",
    "-e", "postman/environment.json",
    "--env-var", f"base_url={base_url}",
    "--reporters", "htmlextra",
    "--reporter-htmlextra-export", report_file,
    "--timeout-request", "10000",  # 10 segundos por request
    "--delay-request", "500"  # 500ms entre requests
]

# En Windows, usar shell=True para encontrar newman.cmd
is_windows = platform.system() == "Windows"
result = subprocess.run(command, capture_output=True, text=True, shell=is_windows)

print(result.stdout)
if result.stderr:
    print(result.stderr)

# Almacenar el timestamp siempre (incluso si Newman falla)
with open(f"{docs_dir}/.last_run.txt", "w") as f:
    f.write(timestamp)

# Verificar que el reporte fue generado
if not os.path.exists(report_file):
    print(f"❌ Error: No se generó el archivo de reporte en {report_file}")
    print("Verifica que Newman se ejecutó correctamente")
    # Crear un reporte básico de error
    error_html = f"""<!DOCTYPE html>
<html>
<head><title>Error en ejecución</title></head>
<body>
<h1>Error en la ejecución de Newman</h1>
<p>No se pudo generar el reporte. Código de salida: {result.returncode}</p>
<pre>{result.stdout}</pre>
<pre>{result.stderr}</pre>
</body>
</html>"""
    with open(report_file, "w") as f:
        f.write(error_html)

# Copiar a docs/ para GitHub Pages (siempre, incluso si falló)
shutil.copy(report_file, f"{docs_dir}/index.html")

if result.returncode != 0:
    print(f"❌ Newman falló con código de salida: {result.returncode}")
    print(f"📁 Resultados guardados en: {results_dir}")
    print("📄 Report publicado en GitHub Pages")
    sys.exit(result.returncode)

# Mensajes informativos
print("✅ Newman ejecución completada correctamente")
print(f"📁 Resultados guardados en: {results_dir}")
print("📄 Report publicado correctamente en GitHub Pages")