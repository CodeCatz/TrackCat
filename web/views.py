from django.template import RequestContext
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib.auth import logout as auth_logout
from api.models import Project
from api.models import UserProfile

def index(request):
	return render_to_response('pages/index.html',{})

def projects(request):
	project_list = Project.objects.all()
	return render(request, 'pages/projects.html',{'project_list': project_list})

def about(request):
	return render(request, 'pages/about.html',{})

def members(request):
	members_list = UserProfile.objects.filter(active=True).order_by('fullname')
	return render(request, 'pages/members.html',{'members_list': members_list})

def member_page(request,user_id):
	user = get_object_or_404(UserProfile, id=user_id)
	return render(request, 'pages/member_page.html',{'user': user})

def events(request):
	return render(request, 'pages/events.html',{})

def gallery(request):
	return render(request, 'pages/gallery.html',{})

def login(request):
	return render(request, 'pages/login.html',{})

def links(request):
	return render(request, 'pages/links.html',{})

def edituser(request):
	return render(request, 'pages/edituser.html',{})

def privacy(request):
	return render(request, 'pages/privacy.html',{})

def project_detail(request,project_id):
	project = get_object_or_404(Project, project_id=project_id)
	return render(request, 'pages/project_detail.html', {'project': project})

def logout(request):
    auth_logout(request)
    return redirect('/')
