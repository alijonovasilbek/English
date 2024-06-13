from django.urls import path
from .views import user_login,register_view
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/', user_login, name='login'),
    path('accounts/login/', user_login, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
]


