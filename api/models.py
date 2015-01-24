from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=100, null=False, blank=False)
	email = models.EmailField(null=False, blank=False)
	profile_picture = image = models.ImageField(upload_to = generate_filename, blank = True)  
	activity_level = (
			("SC", "Sleepy_Cat"),
			("LC", "Lazy_Cat"),
			("AC", "Active_Cat"),
			("MC", "Mentor_Cat"),
	)
	website = models.URLField(null=False)
	bio = models.TextField(max_length=1000,blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	date_of_last_login = models.DateTimeField(auto_now=True)
	date_update = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	project = models.ManyToManyField(Project, related_name="project_name")
	task = models.ManyToManyField(Tasks, related_name="title")
