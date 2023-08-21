
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
# from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from words.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        # 'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(ws_urlpatterns))),
        'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
    }
)