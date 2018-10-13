from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'private']
		labels = {
			'title': 'Title', 
			'content': '', 
			'private': 'Private. Only logged in users will be able to see this post',
			}
		widgets = {
			'content': forms.Textarea(attrs={'cols': 80}), 
			}
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		labels = {
			'content': 'Comment',
			}
		widgets = {
			'content': forms.Textarea(attrs={'cols': 80}),
			}
