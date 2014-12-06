from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Task 
from .models import Member
from .models import Project


def task_list(request):
    tasks = Task.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'TrackCatApp/task_list.html', {'tasks': tasks})
    