from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['user','website']}),
		('Picture',			{'fields': ['profile_picture']}),
		('Biography',		{'fields': ['bio']}),
		('Activity',		{'fields': ['activity_status']}),
		]
	list_display = ('user', 'activity_status')
	list_filter = ('activity_status',)

class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['project_name', 'status_id', 'project_owner']}),
		('Project details',	{'fields': ['project_description', 'project_deadline', 'repository_link', 'website_production', 'website_test', ]}),
		]
	list_display = ('project_name', 'status_id', 'project_deadline','project_owner',)
	list_filter = ('status_id',)

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['title', 'status', 'owner_id', 'assigned_id','project_id']}),
		('Task details',	{'fields': ['description', 'deadline', ]}),
		]
	list_display = ('title', 'status', 'assigned_id','owner_id','project_id')
	list_filter = ('assigned_id',)

admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)

