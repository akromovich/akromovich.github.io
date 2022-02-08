from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request,'blog/index.html')


def about(request):
	return render(request,'blog/about.html')

def contacts(request):
	return render(request,'blog/contact.html')

def news(request):
	return render(request,'blog/news.html')

def project(request):
	return render(request,'blog/project.html')

def projects(request):
	return render(request,'blog/projects.html')

def services(request):
	return render(request,'blog/services.html')