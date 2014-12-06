from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Member
from .models import Project
from .models import Task 

def member_list(request):
    members = Member.objects.all()
    return render(request, 'TrackCat/task_list.html', {'members': members})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'TrackCat/task_list.html', {'projects': projects})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'TrackCat/task_list.html', {'tasks': tasks})
    