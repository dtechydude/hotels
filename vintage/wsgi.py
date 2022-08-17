"""
WSGI config for vintage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

# loading environment variable - olu
vintage = os.path.expanduser('~/vintage_web')
load_dotenv(os.path.join(vintage, '.env'))
# loading environment variable end - olu

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vintage.settings')

application = get_wsgi_application()
