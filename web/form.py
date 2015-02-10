from django import forms

from api.models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project_name', 'project_description','status_id','project_deadline','repository_link','website_production','website_test','project_owner',)
