from django.template import RequestContext 
from django.shortcuts import render_to_response, render 

def index(request):
	return render_to_response('pages/index.html',{})

def projects(request):
	return render(request, 'pages/projects.html',{})

def about(request):
	return render(request, 'pages/about.html',{})

def members(request):
	return render(request, 'pages/members.html',{})

def events(request):
	return render(request, 'pages/events.html',{})

def gallery(request):
	return render(request, 'pages/gallery.html',{})

def login(request):
	return render(request, 'pages/login.html',{})

def links(request):
	return render(request, 'pages/links.html',{})

def sponsors(request):
	return render(request, 'pages/sponsors.html',{})