from django.db import models
from django.utils import timezone
# Create your models here.


class Projects(models.Model):
	PROJECT_STATUS = (
		('O', 'Opened'),
		('I', 'In progress'),
		('C', 'Closed'),
	)
	project_name = models.CharField(max_length=50)
	project_description = models.CharField(max_length=150)
	status_id = models.CharField(max_length=1, choices=PROJECT_STATUS)
	project_deadline = models.DateTimeField()
	repository_link = models.CharField(max_length=300)
	website_prod = models.CharField(max_length=300)
	website_test = models.CharField(max_length=300)
#	project_owner = models.ForeignKey(Users)
	date_created = models.DateTimeField(auto_now_add=True, default=timezone.now)
	date_modified = models.DateTimeField(auto_now=True, default=timezone.now)
