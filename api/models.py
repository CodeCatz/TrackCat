from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

ACTIVITY_LEVEL_CHOICES = (
	('KITTEN', 'New Kitten'),
	('ACTIVE', 'Active Cat'),
	('SLEEPY', 'Sleepy Cat'),
	('MENTOR', 'Mentor Cat'),
)

class UserProfile(models.Model):
	profile_picture = models.ImageField(upload_to=settings.MEDIA_UPLOAD_FOLDER, blank=True)  
	website = models.URLField(blank=True)
	bio = models.TextField(max_length=2000, blank=True)
	activity_status = models.CharField(max_length=50, choices=ACTIVITY_LEVEL_CHOICES, default='KITTEN')
	last_logged_in = models.DateTimeField(auto_now=True, blank=False)
	date_created = models.DateTimeField(auto_now_add=True, blank=False)
	date_updated = models.DateTimeField(auto_now_add=True)

	#Relations
	user = models.OneToOneField(User) 
	def __unicode__(self):
		return self.user.username	

	@receiver(post_save, sender=User)
	def create_profile_for_user(sender, instance=None, created=False, **kwargs):
		if created:
			UserProfile.objects.get_or_create(user=instance)

PROJECT_STATUS_CHOICES = (
	('OPENED', 'Opened'),
	('INPROGRESS', 'In progress'),
	('CLOSED', 'Closed'),
)

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(max_length=50)
	project_description = models.CharField(max_length=150, blank=True)
	status = models.CharField(max_length=15, choices=PROJECT_STATUS_CHOICES, default='OPENED', blank=False)
	project_deadline = models.DateTimeField(blank=True, null=True)
	repository_link = models.URLField(max_length=300)
	website_production = models.URLField(max_length=300, blank=True)
	website_test = models.URLField(max_length=300, blank=True)
	project_owner = models.ForeignKey(UserProfile)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	project_members = models.ManyToManyField(UserProfile, related_name='project_members')
	def __unicode__(self):
		return self.project_name


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

class Event(models.Model):

	title = models.CharField(max_length=255, blank=False, null=False)
	start_date = models.DateTimeField(blank=False, null=False)
	end_date = models.DateTimeField()
	location = models.TextField(max_length=1000, blank=False)
	description = models.TextField(max_length=1000)
	organizer = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

