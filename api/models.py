from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

ACTIVITY_LEVEL_CHOICES = (
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
	profile_picture = models.ImageField(upload_to=settings.MEDIA_UPLOAD_FOLDER, blank=True)  
	website = models.URLField(blank = True)
	bio = models.TextField(max_length=2000,blank=True)
	active = models.BooleanField(default=False)
	activity_status = models.CharField(max_length=2, choices=ACTIVITY_LEVEL_CHOICES)
	last_logged_in = models.DateTimeField(auto_now=True, blank=False)
	date_created = models.DateTimeField(auto_now_add=True, blank=False)
	date_updated = models.DateTimeField(auto_now_add=True)


PROJECT_STATUS_CHOICES = (
	('OPENED', 'Opened'),
	('INPROGRESS', 'In progress'),
	('CLOSED', 'Closed'),
)

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(max_length=50)
	project_description = models.CharField(max_length=150, blank=True)
	status_id = models.CharField(max_length=15, choices=PROJECT_STATUS_CHOICES, default='OPENED')
	project_deadline = models.DateTimeField(blank=True, null=True)
	repository_link = models.URLField(max_length=300)
	website_production = models.URLField(max_length=300, blank=True)
	website_test = models.URLField(max_length=300, blank=True)
	project_owner = models.ForeignKey(UserProfile)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	user_project = models.ManyToManyField(UserProfile, related_name='user_project')

STATUS_CHOICES = (
	('UNASSIGNED', 'Unassigned'),
	('ASSIGNED', 'Assigned'),
	('WORKINGON', 'Working On'),
	('COMPLETED', 'Completed'),
)

class Task (models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='UNASSIGNED')
	assigned_id = models.ForeignKey(User, blank=True, null=True)
	owner_id = models.ForeignKey(UserProfile)
	project_id = models.ForeignKey(Project)
	deadline = models.DateTimeField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
