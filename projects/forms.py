from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('title','author' ,'about', 'github_link')

		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control' }),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'about': forms.Textarea(attrs={'class': 'form-control'}),
			'github_link': forms.TextInput(attrs={'class': 'form-control'}),

		}

