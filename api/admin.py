from django.contrib import admin
from .models import Task
from .models import UserProfile
from .models import Project

admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(Project)
