from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task (models.Model):

	STATUS_CHOICES = (
		('UNASSIGNED', 'Unassigned'),
		('ASSIGNED', 'Assigned'),
		('WORKINGON', 'Working On'),
		('COMPLETED', 'Completed'),
		)

	title = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='UNASSIGNED')
	assigned_id = models.ForeignKey(User, blank=True, null=True)
	owner_id = models.ForeignKey(User)
	project_id models.ForeignKey(Project)
	deadline = models.DateTimeField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

ACTIVITY_LEVEL = (
			("SC", "Sleepy_Cat"),
			("LC", "Lazy_Cat"),
			("AC", "Active_Cat"),
			("MC", "Mentor_Cat"),
	)

class UserProfile(models.Model):
	user = models.OneToOneField(User) 
	#id = models.AutoField(primary_key=True) 
	fullname = models.CharField(max_length=100, blank=False)
	githubuser = models.CharField(max_length=100, null=False, blank=False)
	email = models.EmailField(blank=False)
	profile_picture = models.ImageField(blank = True)  
	website = models.URLField(null=False)
	bio = models.TextField(max_length=2000,blank=True)
	active = models.BooleanField(default=False)
	activity_status = models.CharField(max_length=2, choices=ACTIVITY_LEVEL)
	last_logged_in = models.DateTimeField(auto_now=True, blank=False)
	date_created = models.DateTimeField(auto_now_add=True, blank=False)
	date_updated = models.DateTimeField(auto_now_add=True)
