from django.contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('new', views.new_list, name='new_list'),
    path('users/<str:email>', views.my_lists, name='my_lists'),
]
