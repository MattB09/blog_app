from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
	"""The home page for blog. All blog posts will be shown on this page in reverse chronological order."""
	if request.user.is_authenticated:
		posts = Post.objects.order_by('-posted_on')
	else:
		posts = Post.objects.filter(private=False).order_by('-posted_on')
	context = {'posts': posts}
	return render(request, 'blog/index.html', context)
	

@login_required	
def new_post(request):
	"""Add a new post."""
	if request.method != 'POST':
		# No data submitted; create blank form.
		form = PostForm()
	else:
		# POST data submitted; process data.
		form = PostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return HttpResponseRedirect(reverse('blog:index'))
	
	context = {'form': form}
	return render(request, 'blog/new_post.html', context)
	
def check_owner(request, written_thing):
	"""Check the post belongs to the current user."""
	if written_thing.author != request.user:
		raise Http404	

@login_required
def edit_post(request, post_id):
	"""Edit an existing post."""
	post = Post.objects.get(id=post_id)
	check_owner(request, post)
	
	if request.method != 'POST':
		# No data submitted; return prefilled form.
		form = PostForm(instance=post)
	else:
		# POST data submitted; process data
		form = PostForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blog:index'))
	
	context = {'post': post, 'form': form}
	return render(request, 'blog/edit_post.html', context)

@login_required
def new_comment(request, post_id):
	"""Write a new comment."""
	post = Post.objects.get(id=post_id)
	
	if request.method != 'POST':
		# No data submitted, load blank form
		form = CommentForm()
	else:
		# Data submitted. validate and save
		form = CommentForm(data=request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.author = request.user
			new_comment.post = post
			new_comment.save()
			return HttpResponseRedirect(reverse('blog:index'))
			
	context = {'post': post, 'form': form}
	return render(request, 'blog/new_comment.html', context)

@login_required
def edit_comment(request, comment_id):
	"""Edit a comment."""
	comment = Comment.objects.get(id=comment_id)
	check_owner(request, comment)
	
	if request.method != 'POST':
		# load prefilled form
		form = CommentForm(instance=comment)
	else:
		# data submitted, validate and save
		form = CommentForm(instance=comment, data=request.Post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blog:index'))
			
	context = {'comment': comment, 'form': form}
	return render(request, 'blog/edit_comment.html', context)
