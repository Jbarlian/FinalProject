from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from blog.models import Post, Comment

# Create your views here.
def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you would like to contact us, please email us at','Antikz@gmail.com']})

def loginform(request):
	return render(request, 'personal/loginform.html')

def Logout(request):
	logout(request)
	return redirect('/')

def Login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		return redirect('/loginfailed/')

def Loginfailed(request):
	return render(request, 'personal/loginformerror.html')

def listblog(request):
	queryset=Post.objects.all().order_by("-date")[:25]
	return render(request, 'blog/blog.html', {'object_list':queryset})

def viewblog(request, pk):
	post = Post.objects.get(pk = pk)
	comments = Comment.objects.filter(postid = post)
	return render(request, 'blog/post.html', {'post': post, 'comments' : comments})

def postcomment(request, pk):
	body = request.POST['Comment']
	p = Post.objects.get(pk = pk)
	c = Comment(userid = request.user, postid = p, body = body)
	c.save()
	return redirect('/blog/' + str(pk))