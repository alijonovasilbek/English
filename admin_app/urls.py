from .views import admin, index1
from django.urls import path
from .views import CategoryCreateView,add_dars

urlpatterns=[
    path('adminpanel/',admin,name='admin'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('add-dars/', add_dars, name='add_dars'),
    path('ustozlar/', index1, name='ustoz_list')
]