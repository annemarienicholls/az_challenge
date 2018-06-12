from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ChallengeGroup
from .forms import ChallengeForm

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

def new_challenge(request):
	"""Add a new Challnge Group."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ChallengeForm()
	else:
		# POST data submitted; process data.
		form = ChallengeForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('az_challenges:challenges'))
			
	context = {'form': form}
	return render(request, 'az_challenges/new_challenge.html', context)
