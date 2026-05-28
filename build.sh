#!/usr/bin/env bash

pip install -r requirements.txt

python3 manage.py migrate

echo "
from django.contrib.auth.models import User;

if not User.objects.filter(username='admin').exists():


User.objects.create_superuser(
    'admin',
    'admin@example.com',
    'admin123'
)


" | python3 manage.py shell
