# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.create_user_profile,name='profile'),
    path('read', views.register_users_list,name='read'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log-workout/', views.log_workout, name='log_workout'),
    path('log-meal/', views.log_meal_html, name='log_meal'),
    path('log-hydration/', views.log_hydration, name='log_hydration'),


]

