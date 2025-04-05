import os
from django.core.asgi import get_asgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django ASGI app first to load the app registry
django_asgi_app = get_asgi_application()

# Now safe to import Channels and app-specific modules
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from websocket_app.routing import websocket_urlpatterns

# Define the ASGI application
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})