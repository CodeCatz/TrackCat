from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

	def publish(self):
		self.date_created = timezone.now()
		self.save()

	def __unicode__(self):
		return self.fullname