from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/any_url/', consumers.OneConsumer.as_asgi())
]