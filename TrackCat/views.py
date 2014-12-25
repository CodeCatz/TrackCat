from django.template import RequestContext 
from django.shortcuts import render_to_response, render 

def index(request):
	return render_to_response('pages/index.html',{})

def projects(request):
	return render(request, 'pages/projects.html',{})

def about(request):
	return render(request, 'pages/about.html',{})
