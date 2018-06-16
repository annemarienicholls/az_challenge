from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import ChallengeGroup, Member, Activity, ChallengeType, ActivityType
from .forms import ChallengeForm, MemberForm, ActivityForm

def index(request):
	"""The homepage for A-Z Challenges"""
	return render(request, 'az_challenges/index.html')

@login_required
def challenges(request):
	"""Show all Challenges."""
	challenges = ChallengeGroup.objects.filter(owner=request.user).order_by('date_added')
	challenge_types = ChallengeType.objects.all()
	context = {'challenges': challenges, 'challenge_types': challenge_types}
	return render(request, 'az_challenges/challenges.html', context)

@login_required	
def challenge(request, challenge_id):
	"""Show the Members for the requested Challenge."""
	challenge = ChallengeGroup.objects.get(id=challenge_id)
	
	# Make sure the challenge belongs to the current user.
	if challenge.owner != request.user:
		raise Http404
	
	members = challenge.member_set.order_by('name')
	activities = challenge.activity_set.order_by('category')
	context = {'challenge': challenge, 'members': members, 'activities': activities}
	return render(request, 'az_challenges/challenge.html', context)

@login_required
def new_challenge(request):
	"""Add a new Challenge Group."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ChallengeForm()
	else:
		# POST data submitted; process data.
		form = ChallengeForm(request.POST)
		if form.is_valid():
			new_challenge = form.save(commit=False)
			new_challenge.owner = request.user
			new_challenge.save()
			return HttpResponseRedirect(reverse('az_challenges:challenge', kwargs={'challenge_id': new_challenge.id}))
			
	context = {'form': form}
	return render(request, 'az_challenges/new_challenge.html', context)

@login_required
def new_member(request, challenge_id):
	"""Add a new member to a challenge"""
	challenge = ChallengeGroup.objects.get(id=challenge_id)
	
	if challenge.owner != request.user:
		raise Http404
	
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

@login_required	
def edit_member(request, member_id):
	"""Edit an existing member"""
	member = Member.objects.get(id=member_id)
	challenge = member.challenge_group
	
	if challenge.owner != request.user:
		raise Http404
	
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
	

@login_required
def new_activity(request, challenge_id):
	"""Add a new Activity to a challenge."""
	challenge = ChallengeGroup.objects.get(id=challenge_id)
	
	if challenge.owner != request.user:
		raise Http404
		
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ActivityForm()
		form.fields['owner'].queryset = Member.objects.filter(challenge_group = challenge_id)
		form.fields['activity_type'].queryset = ActivityType.objects.filter(challenge_type = challenge.challenge_type)
	else:
		# POST data submitted; process data
		form = ActivityForm(data=request.POST)
		form.fields['owner'].queryset = Member.objects.filter(challenge_group = challenge_id)
		form.fields['activity_type'].queryset = ActivityType.objects.filter(challenge_type = challenge.challenge_type)
		if form.is_valid():
			new_activity = form.save(commit=False)
			new_activity.challenge_group = challenge
			new_activity.save()
			return HttpResponseRedirect(reverse('az_challenges:challenge', args=[challenge_id]))
			
	context = {'challenge': challenge, 'form': form}
	return render(request, 'az_challenges/new_activity.html', context)



@login_required
def edit_activity(request, activity_id):
	"""Edit an existing activity"""
	activity = Activity.objects.get(id=activity_id)
	challenge = activity.challenge_group
	
	if challenge.owner != request.user:
		raise Http404
	
	if request.method != 'POST':
		# Initial request; pre-fill with the current member
		form = ActivityForm(instance=activity)
		form.fields['owner'].queryset = Member.objects.filter(challenge_group = challenge.id)
		form.fields['activity_type'].queryset = ActivityType.objects.filter(challenge_type = challenge.challenge_type)
	else:
		# POST data submitted; process data
		form = ActivityForm(instance=activity, data=request.POST)
		form.fields['owner'].queryset = Member.objects.filter(challenge_group = challenge.id)
		form.fields['activity_type'].queryset = ActivityType.objects.filter(challenge_type = challenge.challenge_type)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('az_challenges:challenge', args=[challenge.id]))
			
	context = {'activity': activity, 'challenge': challenge, 'form': form}
	return render(request, 'az_challenges/edit_activity.html', context)

@login_required
def edit_challenge(request, challenge_id):
	"""Edit an existing challenge to give it a new name"""
	challenge = ChallengeGroup.objects.get(id=challenge_id)
	
	if challenge.owner != request.user:
		raise Http404
	
	if request.method != 'POST':
		# Initial request; pre-fill with the current challenge
		form = ChallengeForm(instance=challenge)
	else:
		# POST data submitted; process data
		form = ChallengeForm(instance=challenge, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('az_challenges:challenge', args=[challenge.id]))
			
	context = {'challenge': challenge, 'form': form}
	return render(request, 'az_challenges/edit_challenge.html', context)
