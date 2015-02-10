from django.template import RequestContext
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from api.models import Project
from .form import ProjectForm


def index(request):
	return render_to_response('pages/index.html',{})

def projects(request):
	project_list = Project.objects.all()
	return render(request, 'pages/projects.html',{'project_list': project_list})

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

def edituser(request):
	return render(request, 'pages/edituser.html',{})

def privacy(request):
	return render(request, 'pages/privacy.html',{})

def project_detail(request,project_id):
	project = get_object_or_404(Project, project_id=project_id)
	return render(request, 'pages/project_detail.html', {'project': project})

def project_new(request):
	if request.method == "POST":
		projectform = ProjectForm (request.POST)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('web.views.project_detail', project_id=project.project_id)
	else:
		projectform = ProjectForm()
	return render(request, 'pages/project_edit.html', {'projectform': projectform})

def project_edit(request, project_id):
	project = get_object_or_404(Project, project_id=project_id)
	if request.method == "POST":
		projectform = ProjectForm(request.POST, instance=project)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('web.views.project_detail', project_id=project.project_id)
	else:
		projectform = ProjectForm(instance=project)
	return render(request, 'pages/project_edit.html', {'projectform': projectform})
