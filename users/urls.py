from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("dashboard", views.dashboard, name='dashboard')
]