from django import forms

from api.models import Project, PROJECT_STATUS_CHOICES

class ProjectForm(forms.ModelForm):

	project_name = forms.CharField(help_text="type the project name", 
					label="Name",
					widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the project name'}))
	
	project_description = forms.CharField(
					label="Description",
					widget=forms.Textarea(attrs={'class':'form-control','rows':'6','placeholder':'Tell a bit more about the project.'}),
					required=False)
	
	project_deadline = forms.CharField(
					label="Deadline date",
					widget=forms.TextInput(attrs={"id": "id_datepicker", "class": "form-control",
									 "autocomplete": "off","placeholder": "When is the project deadline?"}),
					required=False
						)

	status_id = forms.ChoiceField(
					choices = PROJECT_STATUS_CHOICES,
					label="Status",
					widget= forms.Select(attrs={'class':'form-control'})
				)

	repository_link = forms.CharField( 
					label="Repository",
					widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Where is your repository?'}))
	
	website_test = forms.CharField( 
					label="Test site",
					widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your test site'}),
					required=False
					)

	website_production = forms.CharField( 
					label="Production site",
					widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your production site'}),
					required=False
					)


	class Meta:
		model = Project
		fields = ('project_name', 
				'project_description',
				'status_id',
				'project_deadline',
				'repository_link',
				'website_production',
				'website_test',
				'project_owner',)
