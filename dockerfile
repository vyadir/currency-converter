# Usa imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema necesarias para compilar paquetes
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia dependencias del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Agrega permisos de ejecución al script de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expone el puerto usado por Gunicorn
EXPOSE 8000

# Define el punto de entrada y el comando final
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "cop_currency_converter.wsgi:application", "--bind", "0.0.0.0:8000"]