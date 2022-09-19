from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from sis import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='SIS/registration/login.html'), name='login'),
    path('add/', views.add_student, name='add'),
    # searching
    path('search/', views.SearchResultView.as_view(), name='search'),
    # path('search/<str:pk>', views.search, name='search'),
    path('delete/<str:pk>', views.remove_student, name='delete'),
    path('update/<str:pk>', views.edit_student, name='update'),
    path('remove/<str:pk>/', views.remove_student, name='remove'),
    path('logout/', auth_views.LogoutView.as_view(template_name='SIS/registration/logout.html'), name='logout'),
    path('', views.HomepageView.as_view(), name='home'),
]