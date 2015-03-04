from django import forms
from api.models import UserProfile
from api.models import Project
from api.models import Task

class TaskForm(forms.ModelForm):
	
	class Meta:
		model= Task
		fields = (
			'title',
			'status',
			'owner_id',
			'project_id',
			'description',
			'deadline',
			)

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the task name'}),
			'status': forms.Select(attrs={'class':'form-control '}),
			'owner_id': forms.Select(attrs={'class':'form-control'}),
			'project_id': forms.Select(attrs={'class':'form-control'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'rows':'6','placeholder':'Tell a bit more about the task.'}),
			'project_deadline': forms.TextInput(attrs={'id': 'id_datepicker', 'class': 'form-control datetime-widget',
			'autocomplete': 'off', 'placeholder': 'When is the project deadline?'}),
			'deadline': forms.TextInput(attrs={'id': 'id_datepicker', 'class': 'form-control datetime-widget'}),
		}

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()

	RELATED_FIELD_MAP = {
		'first_name': 'first_name',
		'last_name': 'last_name',
		}

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		if self.instance.id:
			for field, target_field in self.RELATED_FIELD_MAP.items():
				self.initial[ field ] = getattr(self.instance.user, target_field )

	def save(self, *args, **kwargs):
		for field, target_field in self.RELATED_FIELD_MAP.items():
			setattr(self.instance.user,target_field, self.cleaned_data.get(field))
		self.instance.user.save()
		super(UserProfileForm, self).save(*args, **kwargs)

	class Meta:
		model = UserProfile
		fields = (
			'first_name',
			'last_name',
			'profile_picture',
			'website',
			'bio',
			)

class ProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		fields = ('project_name', 
				'project_description',
				'status',
				'project_deadline',
				'repository_link',
				'website_production',
				'website_test',
				'project_owner',
				'project_members',
		)

		widgets = {
				'project_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the project name'}),
				'project_description': forms.Textarea(attrs={'class':'form-control', 'rows':'6','placeholder':'Tell a bit more about the project.'}),
				'project_deadline': forms.TextInput(attrs={'id': 'id_datepicker', 'class': 'form-control datetime-widget',
							'autocomplete': 'off', 'placeholder': 'When is the project deadline?'}),
				'status': forms.Select(attrs={'class':'form-control '}),
				'repository_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Where is your repository?'}),
				'website_production': forms.TextInput(attrs={'class':'form-control','placeholder':'Your test site'}),
				'website_test': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your production site'}),
				'project_owner': forms.Select(attrs={'class':'form-control'}),
				'project_members': forms.SelectMultiple(attrs={'class':'form-control'}),
		}
		
		labels = {
				'project_name': 'Name', 
				'project_description': 'Description',
				'status': 'Status',
				'project_deadline': 'Deadline date',
				'repository_link' :'Repository',
				'website_production': 'Production site',
				'website_test': 'Test site',
				'project_owner': 'Owner',
				'project_members' : 'Project members',
		}

		help_texts = {
			'project_deadline': "Example: YYYY/MM/DD h:m",
			'project_members' : "Select multiple users with ctrl/com key",
		}

		error_messages = {
				'project_name': {
					'required': u'Please enter a name for your project.',
					'invalid': u'Please check if this is a valid name',
				},
				'project_description': {
					'invalid': u'Please check if this is a valid description',
				},
				'status': {
					'required': u'Please select a status for your project.',
					'invalid': u'Please check if this is a valid status',
				},
				'project_deadline':{
					'invalid': u'Please check if this is a valid date',
				},
				'repository_link': {
					'required': u'Please enter a repository url for your project.',
					'invalid': u'Please check if this is a valid url',
				},
				'website_production': {
					'invalid': u'Please check if this is a valid url',
				},
				'website_test': {
					'invalid': u'Please check if this is a valid url',
				},
				'project_owner': {
					'required': u'Please select a project owner.',
					'invalid': u'Please check if this is valid',
				},
				'project_members': {
					'required': u'Please select at least on member for your project.',
					'invalid': u'Please check if there is a member selected',
				},
			}
