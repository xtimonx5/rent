release: python manage.py migrate
release: python manage.py createsuperuser --username admin --password admin
web: gunicorn gettingstarted.wsgi --log-file -
