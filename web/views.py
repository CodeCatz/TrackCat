from django.template import RequestContext
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from api.models import UserProfile, Project, Task, Event

from .form import UserProfileForm, ProjectForm, TaskForm

def index(request):
	return render(request, 'pages/index.html',{})

def projects(request):
	project_list = Project.objects.all()
	return render(request, 'pages/projects.html',{'project_list': project_list})

def about(request):
	return render(request, 'pages/about.html',{})

def members(request):
	members_list = UserProfile.objects.all().filter(user__is_active=True)
	return render(request, 'pages/members.html',{'members_list': members_list})

def member_detail(request,user_id):
	if UserProfile.objects.filter(pk=user_id).exists():
		userprofile = UserProfile.objects.get(pk=user_id)
	else:
		userprofile = None

	return render(request, 'pages/member_detail.html', {'userprofile': userprofile})

@login_required
def member_edit(request):
	if UserProfile.objects.filter(user=request.user).exists():
		userprofile = UserProfile.objects.get(user=request.user)
	else:
		return render(request, 'pages/member_edit.html', {'invalid_userprofile': True})

	if request.method == "POST":
		userprofileform = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if userprofileform.is_valid():
			userprofile = userprofileform.save()
			return redirect('pages-members')
	else:
		userprofileform = UserProfileForm(instance=userprofile)

	return render(request, 'pages/member_edit.html', {'userprofileform': userprofileform})	

def tasks(request):
	task_list = Task.objects.all()
	return render(request, 'pages/tasks.html', {'task_list': task_list})

@permission_required('api.change_task', login_url='/login/')
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

@permission_required('api.add_task', login_url='/login/')
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
	events_list = Event.objects.all().order_by('start_date')
	return render(request, 'pages/events.html',{'events_list': events_list})

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

@permission_required('api.add_project', login_url='/login/')
def project_new(request):
	if request.method == "POST":
		projectform = ProjectForm (request.POST)
		if projectform.is_valid():
			project = projectform.save()
			return redirect('project-detail', project_id=project.project_id)
	else:
		projectform = ProjectForm()

	return render(request, 'pages/project_edit.html', {'projectform': projectform})

@permission_required('api.change_project', login_url='/login/')
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
