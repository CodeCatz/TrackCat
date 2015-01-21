from django.db import models

# Create your models here.

from django.db import models

class Projects(models.Model):
	PROJECT_STATUS = (
		('O', 'Opened'),
		('I', 'In progress'),
		('C', 'Closed'),
	)
	project_name = models.CharField(max_length=50)
	project_description = models.CharField(max_length=150)
	status_id = models.CharField(max_length=1, choices=PROJECT_STATUS)
	project_deadline = models.DateField()
	repository_link = models.CharField(max_length=300)
	website_prod = models.CharField(max_length=300)
	website_test = models.CharField(max_length=300)
#	project_owner = models.ForeignKey(Users)
	date_created = models.DateField()
	project_owner = models.DateField()
