#!/usr/bin/env bash
set -o errexit

pip install django-recaptcha
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate