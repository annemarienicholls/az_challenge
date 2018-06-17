from django import forms

from .models import ChallengeGroup, Member, Activity

class ChallengeForm(forms.ModelForm):
	class Meta:
		model = ChallengeGroup
		fields = ['name', 'challenge_type']
		labels = {'name': 'Challenge Team Name', 'challenge_type': 'Type of Challenge'}

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['name']
		labels = {'name': ''}

class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		fields=['owner', 'activity_type', 'details', 'date_completed']
		labels = {'owner': 'Team Member who owns activity', 'activity_type': 'Letter of Activity (ignore if custom)',
					'details': 'Activity chosen', 'date_completed': 'Date activity completed'
				}
		
	date_completed = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date'}))



