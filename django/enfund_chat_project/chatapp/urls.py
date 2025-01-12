from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    path('accounts/', include('django.contrib.auth.urls')),
]