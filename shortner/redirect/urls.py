from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_links, name='my_links'),
    path('get', views.echo, name='get'),
]
