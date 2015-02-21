from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
	fields = (('user', 'fullname'), 'githubuser' )


admin.site.register(Task)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Project)
