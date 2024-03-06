from django.urls import path
from . import views

urlpatterns = [
    path('handbook/categories/', views.handbook, name='app_list'),
    path('handbook/categories/create/', views.handbook, name='app_create'),
    path('handbook/categories/<int:pk>/', views.category_detail, name='app_detail'),
    path('handbook/categories/update/<int:pk>/', views.category_detail, name='app_update'),
    path('handbook/categories/delete/<int:pk>/', views.category_detail, name='app_delete'),
]