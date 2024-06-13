from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_chat, name='room_chat'),
    path('create_room/', views.create_room, name='create_room'),
]
