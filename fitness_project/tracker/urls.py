# urls.py
from django.urls import path
from . import views


urlpatterns = [
     path('users', views.create_user_profile,name='profile'),
     path('read', views.register_users_list,name='read'),
     path('log-meal-ui/', views.log_meal_html, name='log_meal_html'),
]

