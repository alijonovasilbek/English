from django.urls import  path
from .views import register_view,logout_view,login_view,change_password

urlpatterns=[
    path('register/',register_view,name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password, name='password_change'),

]