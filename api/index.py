import os
from django.core.wsgi import get_wsgi_application

# Ensure Django settings module is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')

# Initialize the WSGI application once (cold-start friendly)
application = get_wsgi_application()

def handler(event, context):
    """Vercel expects a `handler(event, context)` function.
    We forward the request to Django's WSGI app via a tiny helper.
    """
    from vercel_wsgi import run_wsgi
    return run_wsgi(application, event, context)
