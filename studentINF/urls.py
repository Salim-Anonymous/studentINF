"""studentINF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='SIS/registration/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='SIS/index.html'), name='home'),
]
