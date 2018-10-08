from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
		labels = {'title': 'Title', 'content': ''}
		widgets = {'content': forms.Textarea(attrs={'cols': 80})}
		
		
