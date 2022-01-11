import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chats.routing
from chats.custommiddleware import JwtAuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roof.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": JwtAuthMiddlewareStack(
        URLRouter(
            chats.routing.websocket_urlpatterns
        )
    ),
})
