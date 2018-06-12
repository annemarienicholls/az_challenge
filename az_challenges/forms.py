from django import forms

from .models import ChallengeGroup

class ChallengeForm(forms.ModelForm):
	class Meta:
		model = ChallengeGroup
		fields = ['name']
		labels = {'name': 'Challenge Name'}
