from django.template import RequestContext
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from api.models import UserProfile
from api.models import Project
from .form import UserProfileForm
from .form import ProjectForm
from django.contrib.auth import logout as auth_logout
from api.models import Project
from api.models import Task
from .form import TaskForm
from django.contrib.auth.decorators import login_required

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
	user = get_object_or_404(UserProfile, id=user_id)
	return render(request, 'pages/member_page.html',{'user': user})

def user_edit(request, user_id):
	user = get_object_or_404(UserProfile, id=user_id)
	if request.method == "POST":
		userprofileform = UserProfileForm(request.POST, request.FILES, instance=user)
		if userprofileform.is_valid():
			user = userprofileform.save()
			return redirect('pages-member-detail', user_id)
	else:
		userprofileform = UserProfileForm(instance=user)

	return render(request, 'pages/edituser.html', {'userprofileform': userprofileform})	

def tasks(request):
	task_list = Task.objects.all()
	return render(request, 'pages/tasks.html', {'task_list': task_list})

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

	return render(request, 'pages/task_edit.html', {'taskform': taskform,
									'editing': True})

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
