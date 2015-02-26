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
		(None,				{'fields': ['project_name', 'status', 'project_owner']}),
		('Project details',	{'fields': ['project_description', 'project_deadline', 'repository_link', 'website_production', 'website_test', ]}),
		]
	list_display = ('project_name', 'status', 'project_deadline','project_owner',)
	list_filter = ('status',)

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['title', 'status', 'owner_id', 'assigned_id','project_id']}),
		('Task details',	{'fields': ['description', 'deadline', ]}),
		]
	list_display = ('title', 'status', 'assigned_id','owner_id','project_id')
	list_filter = ('assigned_id',)

class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['title', 'description', 'organizer']}),
		('Time and place',	{'fields': ['start_date', 'end_date', 'location' ]}),
		]
	list_display = ('title', 'start_date', 'end_date','location')

admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)

