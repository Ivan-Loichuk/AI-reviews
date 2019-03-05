from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from application import views

urlpatterns = [
    path('add', csrf_exempt(views.create_hotel), name='add'),
    path('registration', csrf_exempt(views.registration), name='registration'),
    path('auth', csrf_exempt(views.auth), name='auth'),
    path('logout', csrf_exempt(views.user_logout), name='user_logout'),
    path('all', views.get_hotels, name='all')
]
