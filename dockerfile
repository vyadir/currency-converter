# Usa imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Recolecta archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto usado por Gunicorn
EXPOSE 8000

# Comando de inicio en producción
CMD ["gunicorn", "cop_currency_converter.wsgi:application", "--bind", "0.0.0.0:8000"]