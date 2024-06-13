from . import views
from .views import index
from django.urls import path
from .views import CategoryListView, CategoryDetailView, DarsListView, DarsDetailView

urlpatterns = [
    path('',index , name='main'),
]

urlpatterns += [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('dars/', DarsListView.as_view(), name='dars_list'),
    path('dars/<int:pk>/', DarsDetailView.as_view(), name='dars_detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('like_post',views.like_post,name='like'),
    path('increment_view_count/<int:pk>/', views.increment_view_count, name='increment_view_count'),

]
