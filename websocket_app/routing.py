from django.urls import re_path
from websocket_app.consumers import LangflowConsumer

websocket_urlpatterns = [
    re_path(r"^ws/langflow/$", LangflowConsumer.as_asgi()),
]
