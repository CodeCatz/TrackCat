from django.shortcuts import render

from .models import Member
from .models import Project
from .models import Task 

def index(request):
    members = Member.objects.all()
    #completed_projects = Project.objects.filter(published_date__isnull=False).order_by('published_date')
    completed_projects = Project.objects.all()
    active_members = Member.objects.all()
    return render(request, 'TrackCat/index.html', {'completed_projects': completed_projects}) 
    return render(request, 'TrackCat/index.html', {'active_members': active_members})  
    #return render(request, 'TrackCat/index.html', {})   

def member_list(request):
    members = Member.objects.all()
    return render(request, 'TrackCat/members.html', {'members': members})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'TrackCat/projects.html', {'projects': projects})

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'TrackCat/tasks.html', {'tasks': tasks})


    