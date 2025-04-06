# !/bin/bash
source opt/venv/bin/activate
cd / code

python manage.py sendtestemail --admins
python manage.py migrate --no-input
python manage.py auto_admin

export RUNTIME_PORT=8000

# add static files to the container on runtime
# python manage.py collectstatic --no-input
waitress-serve --port=$RUNTIME_PORT home.wsgi:application