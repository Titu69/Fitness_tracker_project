from django.urls import path
from . import views
urlpatterns=[
    path('',views.register_view,name='register'),
    path('readdata',views.register_users_list, name='register_users_list'),
    path('logindata/<str:username>/',views.login_users_list, name='login_users_list'),
    path('login',views.login_view,name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'), 
]
""" 
from django.urls  import path,include
from rest_framework.routers import  DefaultRouter
from .views import ProfilesViewSet
router=DefaultRouter()
router.register(r'view',ProfilesViewSet)
urlpatterns=[
    path('',include(router.urls)),
] """