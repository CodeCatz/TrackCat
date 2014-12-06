from django.contrib import admin
from .models import Task
from .models import Member
from .models import Project

admin.site.register(Task)
admin.site.register(Member)
admin.site.register(Project)