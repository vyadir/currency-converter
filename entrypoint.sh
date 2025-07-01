#!/bin/sh

# Ejecuta migraciones de base de datos
python manage.py migrate --noinput

# Recolecta archivos estáticos para producción
python manage.py collectstatic --noinput

# Ejecuta el comando recibido (Gunicorn)
exec "$@"