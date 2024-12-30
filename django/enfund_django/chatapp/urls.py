from django.urls import path
from . import views

urlpatterns = [
    # path('chat/', chat_view, name='chat'),
    path('chat/<str:room_name>', views.room, name='room'),
]