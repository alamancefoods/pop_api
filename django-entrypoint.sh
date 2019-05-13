#!/bin/sh
echo Running Django Migrations.
cd pop_api
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


echo Starting Gunicorn
gunicorn pop_api.wsgi:application --name pop_api --bind 127.0.0.1:8000 --workers 1 --daemon
echo Starting Envoy Reverse Proxy
cd ..
envoy -c django-service-envoy.yaml --service-cluster pop_web


