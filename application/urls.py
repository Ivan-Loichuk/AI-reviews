from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from application import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', csrf_exempt(views.create_hotel), name='add'),
    path('all', views.get_hotels, name='all')
]
