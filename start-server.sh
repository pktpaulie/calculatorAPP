# !/git/usr/bin/bash
# C:\Users\dell\Documents\Bootcamp\CICID\calculator_proj\start-server.sh
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd calculator_proj; python manage.py createsuperuser --no-input)
fi
(cd calculator_proj; gunicorn calculator_proj.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"

#  to run execute (icacls start-server.sh)