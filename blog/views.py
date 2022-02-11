from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Work,Articles
from .forms import ArticlesForm


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
	art = Articles.objects.all()
	error = ''
	if request.method == 'POST':
		form = ArticlesForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = "Форма была неверной"

	post = Post.objects.get(id=pk)
	form  =ArticlesForm()
	context = {
		'forms':form,
		"all_posts":post,
		'error':error,
		'arts':art
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