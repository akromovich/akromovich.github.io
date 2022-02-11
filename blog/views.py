from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Work


def index(request):
	work = Work.objects.all()
	context = {
		"works":work
	}
	return render(request,'blog/index.html',context)


def about(request):
	return render(request,'blog/about.html')

def contacts(request):
	return render(request,'blog/contact.html')

def news(request):
	return render(request,'blog/news.html')

def project(request,pk):
	post = Post.objects.get(id=pk)
	context = {
		"all_posts":post
	}
	return render(request,'blog/project.html',context)

def projects(request):
	posts = Post.objects.all()
	context = {
		'posts':posts
	}
	return render(request,'blog/projects.html',context)

def services(request):
	return render(request,'blog/services.html')