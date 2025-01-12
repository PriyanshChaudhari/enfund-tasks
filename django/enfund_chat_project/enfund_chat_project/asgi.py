"""
ASGI config for enfund_chat_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enfund_chat_project.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from . import routing

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() ,
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )   
        )
    }
)