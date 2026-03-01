import time
import subprocess
import os
import sys
import shutil

# Creación de timestamp
timestamp = time.strftime("%Y%m%d_%H%M%S")

# Definir directorios
results_dir = f"results/run_{timestamp}"
docs_dir = "docs"

os.makedirs(results_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

# BASE_URL por defecto para pruebas en local (prioridad: CLI > ENV > default)
base_url = os.getenv("BASE_URL", "http://localhost:8000")

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
    "--env-var", f"BASE_URL={base_url}",
    "--reporters", "htmlextra",
    "--reporter-htmlextra-export", report_file
]

result = subprocess.run(command, shell=True, capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print(result.stderr)

# Copiar a docs/ para GitHub Pages (siempre, incluso si falló)
shutil.copy(report_file, f"{docs_dir}/index.html")

# Almacena el ultimo timestamp ejecutado
with open(f"{docs_dir}/.last_run.txt", "w") as f:
    f.write(timestamp)

if result.returncode != 0:
    print(f"❌ Newman falló con código de salida: {result.returncode}")
    print(f"📁 Resultados guardados en: {results_dir}")
    print("📄 Report publicado en GitHub Pages")
    sys.exit(result.returncode)

# Mensajes informativos
print("✅ Newman ejecución completada correctamente")
print(f"📁 Resultados guardados en: {results_dir}")
print("📄 Report publicado correctamente en GitHub Pages")