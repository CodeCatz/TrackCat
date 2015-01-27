from django.db import models
from django.utils import timezone
# Create your models here.

class Task (models.Model):

	STATUS_CHOICES = (
		('UNASSIGNED', 'Unassigned'),
		('WORKINGON', 'Working On'),
		('COMPLETED', 'Completed'),
		)

	title = models.CharField(max_length=255, default=None)
	description = models.TextField(max_length=1000)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='UNASSIGNED')
	#assigned_id = models.ForeignKey(User)
	#owner_id = models.ForeignKey(User)
	#project_id models.ForeignKey(Project)
	deadline = models.DateTimeField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)
	