"""Defines URL patterns for blog"""

from django.urls import path
from . import views

urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	
	# New post
	path('new_post/', views.new_post, name='new_post'),
	
	# Edit post
	path('edit_post/<post_id>', views.edit_post, name='edit_post'),
	
	# New comment
	path('<post_id>/new_comment', views.new_comment, name='new_comment'),
	
	# Edit comment
	path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
]
