from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'), 
    path('profile/settings/update_user/', views.update_user, name="update_user"),
    path('profile/settings/update_password/', views.update_password, name="update_password"),
    
]