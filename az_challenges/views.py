from django.shortcuts import render

from .models import ChallengeGroup

def index(request):
	"""The homepage for A-Z Challenges"""
	return render(request, 'az_challenges/index.html')

def challenges(request):
	"""Show all Challenges."""
	challenges = ChallengeGroup.objects.order_by('date_added')
	context = {'challenges': challenges}
	return render(request, 'az_challenges/challenges.html', context)
	
def challenge(request, challenge_id):
	"""Show the Members for the requested Challenge."""
	challenge = ChallengeGroup.objects.get(id=challenge_id)
	members = challenge.member_set.order_by('name')
	context = {'challenge': challenge, 'members': members}
	return render(request, 'az_challenges/challenge.html', context)
