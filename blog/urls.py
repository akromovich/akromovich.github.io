from django.urls import path
from . import views



urlpatterns = [
	path('',views.index,name='index'),
	path('about/',views.about,name='about'),
	path('contacts/',views.contacts,name='contacts'),
	path('news/',views.news,name='news'),
	path('project/',views.project,name='project'),
	path('projects/',views.projects,name='projects'),
	path('services/',views.services,name='services'),
]








