from django import forms

from .models import ChallengeGroup, Member

class ChallengeForm(forms.ModelForm):
	class Meta:
		model = ChallengeGroup
		fields = ['name']
		labels = {'name': 'Challenge Name'}

class MemberForm(forms.ModelForm):
	
	class Meta:
		model = Member
		fields = ['name']
		labels = {'name': ''}
