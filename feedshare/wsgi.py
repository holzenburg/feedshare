"""
WSGI config for feedshare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

try:
    activate_this = "/srv/python/virtualenv/arne_feedshare/bin/activate_this.py"
    execfile(activate_this, dict(__file__=activate_this))
except:
    pass

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedshare.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

