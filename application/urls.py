from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from application.views import hotel_view, security_view

urlpatterns = [
    path('api/add', csrf_exempt(hotel_view.create_hotel), name='add'),
    path('api/registration', csrf_exempt(security_view.registration), name='registration'),
    path('api/auth', csrf_exempt(security_view.auth), name='auth'),
    path('api/logout', csrf_exempt(security_view.user_logout), name='user_logout'),
    path('api/all', hotel_view.get_hotels, name='all'),
    path('api/hotel/<int:hotel_id>', hotel_view.get_hotel, name='get_hotel'),
    path('api/type', hotel_view.add_hotel_type, name='add_hotel_type'),
    path('api/hotel/comment', hotel_view.add_comment, name='add_comment'),
    path('api/hotels/search', hotel_view.search_hotels, name='search_hotels'),
    path('api/hotel/<int:hotel_id>/comments', hotel_view.get_comments, name='get_Comments'),
    path('api/hotel/<int:hotel_id>/statistic', hotel_view.get_statistic, name='hotel_statistic'),
    path('api/hotel/<int:hotel_id>/comment-mappings', hotel_view.get_comment_mappings, name='comment_mappings')
]
