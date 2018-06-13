from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ChallengeGroup, Member
from .forms import ChallengeForm, MemberForm

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
	"""Add a new Challenge Group."""
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



def new_member(request, challenge_id):
	"""Add a new member to a challenge"""
	challenge = ChallengeGroup.objects.get(id=challenge_id)
	
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = MemberForm()
	else:
		# POST data submitted; process data
		form = MemberForm(data=request.POST)
		if form.is_valid():
			new_member = form.save(commit=False)
			new_member.challenge_group = challenge
			new_member.save()
			return HttpResponseRedirect(reverse('az_challenges:challenge', args=[challenge_id]))
			
	context = {'challenge': challenge, 'form': form}
	return render(request, 'az_challenges/new_member.html', context)
	
def edit_member(request, member_id):
	"""Edit an existing member"""
	member = Member.objects.get(id=member_id)
	challenge = member.challenge_group
	
	if request.method != 'POST':
		# Initial request; pre-fill with the current member
		form = MemberForm(instance=member)
	else:
		# POST data submitted; process data
		form = MemberForm(instance=member, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('az_challenges:challenge', args=[challenge.id]))
			
	context = {'member': member, 'challenge': challenge, 'form': form}
	return render(request, 'az_challenges/edit_member.html', context)
	
