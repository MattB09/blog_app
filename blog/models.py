from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	"""A blog post the user posts"""
	title = models.CharField(max_length=255)
	content = models.TextField()
	posted_on = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	private = models.BooleanField(default=False)
	
	def __str__(self):	
		"""Return a string representation of the model."""
		return self.title

class Comment(models.Model):
	"""A model that represents comments on posts."""
	content = models.TextField()
	posted_on = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
	
	def __str__(self):
		"""Returns a string representation of the model."""
		return self.content
