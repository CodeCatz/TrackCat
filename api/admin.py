from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['user', 'fullname', 'githubuser', 'email','website']}),
		('Biography',		{'fields': ['bio']}),
		('Activity',		{'fields': ['active','activity_status']}),
		]
	list_display = ('user', 'fullname', 'githubuser', 'activity_status')
	list_filter = ('activity_status',)

admin.site.register(Task)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project)

