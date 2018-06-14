from django import forms

from .models import ChallengeGroup, Member, Activity

class ChallengeForm(forms.ModelForm):
	class Meta:
		model = ChallengeGroup
		fields = ['name']
		labels = {'name': 'Challenge Team Name'}

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['name']
		labels = {'name': ''}

class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		fields=['owner', 'category', 'details', 'date_completed']
		labels = {'owner': 'Team Member who owns activity',
					'category': 'Letter of alphabet', 'details': 'Activity chosen',
					'date_completed': 'Date activity completed'
				}
		
	date_completed = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	

