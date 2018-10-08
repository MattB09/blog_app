"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	# Login page
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	
	# Logout page
	path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	
	# Registration page
	path('register/', views.register, name='register'),
]
