from django.urls import path
from . import views



app_name = 'chat'

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup_view, name='signup')
]
