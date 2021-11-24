release: python manage.py migrate --noinput
release: python manage.py migrate --fake
web: gunicorn housing.wsgi