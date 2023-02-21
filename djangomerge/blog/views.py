from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, User, Category, Tag, Comment
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from django.contrib.auth.forms import AuthenticationForm
#from taggit.models import Tag

def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
	# Post.objects.get(pk=pk)
	post = get_object_or_404(Post, slug=slug)
	categories = Category.objects.all()
	tags = Tag.objects.all()
	comments = Comment.objects.filter(post=post)
	print(comments)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			try :
				parent = request.POST.get('comment_id')
				parent = Comment.objects.filter(id = parent).last()
				print(parent, 'parent instanceeeee')
			except:
				parent=None
			#print(parent,'aaaaaaaaaaaaaaaaaaa')
			comments = form.save(commit=False)
			comments.post = post
			comments.parent = parent
			comments.save()
		return redirect('blog:post_detail', slug=post.slug)
	else:
		form  = CommentForm()
	return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories,'tags': tags, 'form':form,'comment':comments})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', slug=post.slug)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_detail', slug=post.slug)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def signup_request(request):
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("blog:post_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserForm()
	return render(request=request, template_name="blog/signup.html", context={'form':form})

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			print(user)
			if user:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("blog:post_list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:       
		form = LoginForm()
	return render(request=request, template_name="blog/login.html", context={"form":form})

def logout_request(request):
	logout(request)
	return redirect('blog:login')

def profile_request(request):
	user = get_object_or_404(User, pk=request.user.id)
	return render(request, "blog/profile.html", {'user': user})

def profile_edit(request):
	user = get_object_or_404(User, pk=request.user.id)
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			# user = form.save(commit=False)
			# user.username = request.user
			user.save()
			return redirect('blog:users-profile')
	else:
		form = UserForm(instance=user)
	return render(request, 'blog/signup.html', {'form': form})

def category(request,slug):
	posts = Post.objects.filter(category__slug=slug)#.filter(published_date=True)
	requested_category = Category.objects.get(slug=slug)
	categories = Category.objects.all()
	tags = Tag.objects.all()

	return render (request, 'blog/categories.html', {'posts': posts,
		'category': requested_category,
		'categories': categories,
		'tags': tags,}) # blog/category_list.html should be the template that categories are listed.

def tag(request, slug):
	posts = Post.objects.filter(tag__slug=slug)
	requested_tag = Tag.objects.get(slug=slug)
	categories = Category.objects.all()
	tags = Tag.objects.all()
	return render(request, 'blog/tags.html', {'posts': posts,
		'tag': requested_tag,
		'categories': categories,
		'tags': tags, })
