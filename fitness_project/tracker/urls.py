# urls.py
from django.urls import path
from . import views

""" urlpatterns = [
    # UserProfiles
    path('users/', UserProfileAPIView.as_view()),
    path('users/<str:pk>/', UserProfileAPIView.as_view()),

    # Workouts
    path('workouts/', WorkoutAPIView.as_view()),
    path('workouts/<str:pk>/', WorkoutAPIView.as_view()),

    # Meals
    path('meals/', MealAPIView.as_view()),
    path('meals/<str:pk>/', MealAPIView.as_view()),

    # Hydration
    path('hydration/', HydrationAPIView.as_view()),
    path('hydration/<str:pk>/', HydrationAPIView.as_view()),
] """
urlpatterns = [
     path('users/', views.create_user_profile,name='profile'),
     path('read', views.register_users_list,name='read'),

     

]

