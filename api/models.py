from django.db import models

class Task (models.Model):

	STATUS_CHOICES = (
		('UNASSIGNED', 'Unassigned'),
		('WORKINGON', 'Working On'),
		('COMPLETED', 'Completed'),
		)

	title = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True)
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='UNASSIGNED')
	#assigned_id = models.ForeignKey(User)
	#owner_id = models.ForeignKey(User)
	#project_id models.ForeignKey(Project)
	deadline = models.DateTimeField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
