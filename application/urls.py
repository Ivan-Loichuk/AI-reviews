from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from application import views
from application import security_view

urlpatterns = [
    path('api/add', csrf_exempt(views.create_hotel), name='add'),
    path('api/registration', csrf_exempt(security_view.registration), name='registration'),
    path('api/auth', csrf_exempt(security_view.auth), name='auth'),
    path('api/logout', csrf_exempt(security_view.user_logout), name='user_logout'),
    path('api/all', views.get_hotels, name='all'),
    path('api/hotel/<int:hotel_id>', views.get_hotel, name='get_hotel'),
    path('api/type', views.add_hotel_type, name='name=add_hotel_type'),
    path('api/hotel/comment', views.add_comment, name='name=add_hotel_type'),
    path('api/hotel/<int:hotel_id>/comments', views.get_comments, name='name=add_hotel_type')
]
