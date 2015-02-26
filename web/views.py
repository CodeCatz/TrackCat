from django.template import RequestContext
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from api.models import UserProfile, Project, Task

from .form import UserProfileForm, ProjectForm, TaskForm

def index(request):
	return render(request, 'pages/index.html',{})

def projects(request):
	project_list = Project.objects.all()
	return render(request, 'pages/projects.html',{'project_list': project_list})

def about(request):
	return render(request, 'pages/about.html',{})

def members(request):
	members_list = UserProfile.objects.all().order_by('activity_status')
	return render(request, 'pages/members.html',{'members_list': members_list})

def member_page(request,user_id):
	if UserProfile.objects.filter(pk=user_id).exists():
		userprofile = UserProfile.objects.get(pk=user_id)
	else:
		userprofile = None

	return render(request, 'pages/member_page.html', {'userprofile': userprofile})

@login_required
def user_edit(request):
	if UserProfile.objects.filter(user=request.user).exists():
		userprofile = UserProfile.objects.get(user=request.user)
	else:
		return render(request, 'pages/edituser.html', {'invalid_userprofile': True})

	if request.method == "POST":
		userprofileform = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if userprofileform.is_valid():
			userprofile = userprofileform.save()
			return redirect('pages-members')
	else:
		userprofileform = UserProfileForm(instance=userprofile)

	return render(request, 'pages/edituser.html', {'userprofileform': userprofileform})	

def tasks(request):
	task_list = Task.objects.all()
	return render(request, 'pages/tasks.html', {'task_list': task_list})

@login_required
def task_edit(request, task_id):
	if Task.objects.filter(pk=task_id).exists():
		task = Task.objects.get(pk=task_id)
	else:
		return render(request, 'pages/task_edit.html', {'invalid_task_id': True})

	if request.method == "POST":
		taskform = TaskForm(request.POST, instance=task)
		if taskform.is_valid():
			task = taskform.save()
			return redirect('pages-tasks')
	else:
		taskform = TaskForm(instance=task)

	return render(request, 'pages/task_edit.html', {'taskform': taskform, 'editing': True})

@login_required
def task_new(request):
	if request.method == "POST":
		taskform = TaskForm(request.POST)
		if taskform.is_valid():
			task = taskform.save()
			return redirect('pages-tasks')
	else:
		taskform = TaskForm()

	return render(request, 'pages/task_new.html', {'taskform': taskform})

def events(request):
	return render(request, 'pages/events.html',{})

def gallery(request):
	return render(request, 'pages/gallery.html',{})

def login(request):
	return render(request, 'pages/login.html',{})

def links(request):
	return render(request, 'pages/links.html',{})

def privacy(request):
	return render(request, 'pages/privacy.html',{})

def project_detail(request, project_id):
	if Project.objects.filter(pk=project_id).exists():
		project = Project.objects.get(pk=project_id)
	else:
		project = None

	return render(request, 'pages/project_detail.html', {'project': project})

@login_required
def project_new(request):
	if request.method == "POST":
		projectform = ProjectForm (request.POST)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('project-detail', project_id=project.project_id)
	else:
		projectform = ProjectForm()

	return render(request, 'pages/project_edit.html', {'projectform': projectform})

@login_required
def project_edit(request, project_id):
	if Project.objects.filter(pk=project_id).exists():
		project = Project.objects.get(pk=project_id)
	else:
		return render(request, 'pages/project_edit.html', {'invalid_project_id': True})

	if request.method == "POST":
		projectform = ProjectForm(request.POST, instance=project)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('project-detail', project_id=project.project_id)
	else:
		projectform = ProjectForm(instance=project)

	return render(request, 'pages/project_edit.html', {'projectform': projectform,
														'editing': True})

def logout(request):
	auth_logout(request)
	return redirect('/')
