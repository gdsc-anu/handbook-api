from django.urls import path
from . import views


urlpatterns = [
    path('handbook/categories/', views.handbook, name='categories_list'),
    
    path('handbook/<slug:slug>/', views.category_detail, name='categories_detail'),
    
    path('handbook/<slug:category_slug>/entries/', views.category_entries, name='category_entries_list'),
    
    path('handbook/<slug:category_slug>/<slug:entry_slug>/', views.category_entry_detail, name='category_entries_detail'),
]


"""
urlpatterns = [
    path('handbook/categories/', views.handbook, name='categories_list'),
    path('handbook/categories/create/', views.handbook, name='categories_create'),
    path('handbook/categories/<int:pk>/', views.category_detail, name='categoriescategories_detail'),
    path('handbook/categories/update/<int:pk>/', views.category_detail, name='categories_update'),
    path('handbook/categories/delete/<int:pk>/', views.category_detail, name='categories_delete'),
    path('handbook/entries/', views.entry, name='entries_list'),
    path('handbook/entries/create/', views.entry, name='entries_create'),
    path('handbook/entries/<int:pk>/', views.entry_detail, name='entries_detail'),
    path('handbook/entries/update/<int:pk>/', views.entry_detail, name='entries_update'),
    path('handbook/entries/delete/<int:pk>/', views.entry_detail, name='entries_delete'),
]
"""