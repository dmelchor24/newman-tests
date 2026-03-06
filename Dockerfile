# Usar imagen base de Node.js (Newman requiere Node)
FROM node:18-alpine

# Instalar Python para el script de ejecución
RUN apk add --no-cache python3 py3-pip

# Crear directorio de trabajo
WORKDIR /app

# Instalar Newman y el reporter
RUN npm install -g newman newman-reporter-htmlextra

# Copiar archivos del proyecto
COPY postman/ ./postman/
COPY scripts/ ./scripts/
COPY docs/ ./docs/

# Crear directorios necesarios
RUN mkdir -p results docs

# Variable de entorno por defecto
ENV base_url=https://endpoints-fast-api.onrender.com

# Comando por defecto
CMD ["python3", "scripts/execute-tests.py"]
