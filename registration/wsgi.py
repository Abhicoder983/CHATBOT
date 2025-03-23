import os
import logging
from django.core.wsgi import get_wsgi_application

logging.basicConfig(level=logging.DEBUG)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registration.settings')

application = get_wsgi_application()

app=application
