from django.urls import path

from SIS import views

urlpatterns = [
    path('sis/', views.index, name='index'),
    path('login/', views.login, name='login'),
]