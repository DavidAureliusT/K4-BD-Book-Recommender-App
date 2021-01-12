from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('first-5-books/', views.firstRating, name='firstrating'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', views.logout, name='logout'),
]
