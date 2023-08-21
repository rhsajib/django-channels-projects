from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
    path('random/', views.one, name='one'),
]
