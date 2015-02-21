from django.contrib import admin
from .models import *

class ProjectInline(admin.TabularInline):
	model = Project

class UserProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['user', 'fullname', 'githubuser', 'email','website']}),
		('Biography',		{'fields': ['bio']}),
		('Activity',		{'fields': ['active','activity_status']}),
		]
	list_display = ('user', 'fullname', 'githubuser', 'activity_status')
	list_filter = ('activity_status',)
	inlines = [
		ProjectInline,
		]

class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['project_name', 'status_id', 'project_owner']}),
		('Project details',	{'fields': ['project_description', 'project_deadline', 'repository_link', 'website_production', 'website_test', ]}),
		]
	list_display = ('project_name', 'status_id', 'project_deadline',)
	list_filter = ('status_id',)

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['title', 'status', 'owner_id', 'project_id']}),
		('Task details',	{'fields': ['description', 'deadline', ]}),
		]
	list_display = ('title', 'status', 'assigned_id',)
	list_filter = ('assigned_id',)

admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)

