#!/bin/bash
echo "Create migrations"
python manage.py makemigrations djangoapp
echo "==========================================="

echo "Migrate"
python manage.py migrate
echo "==========================================="

echo "Run server"
python manage.py runserver 0.0.0.0:8000