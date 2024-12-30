"""
ASGI config for enfund_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chatapp.routing import websocket_urlpatterns
import chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enfund_django.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack( # Include AuthMiddlewareStack if you need authentication
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )
    ),
    # Just include "websocket" in the ProtocolTypeRouter if you don't need authentication:
    # "websocket": URLRouter(
    #     myapp.routing.websocket_urlpatterns
    # ),

})