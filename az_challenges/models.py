from django.db import models
from django.contrib.auth.models import User

class ChallengeType(models.Model):
	"""Type of challenge, e.g. A-Z or other"""
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
		
class ActivityType(models.Model):
	"""Type of activity, linked to ChallengeType"""
	name = models.CharField(max_length=20)
	challenge_type = models.ForeignKey(ChallengeType, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
	

class ChallengeGroup(models.Model):
	"""Links people with activities for a single challenge"""
	challenge_type = models.ForeignKey(ChallengeType, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.name
		

class Member(models.Model):
	"""People who are in the Challenge Group."""
	challenge_group = models.ForeignKey(ChallengeGroup, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.name

class Activity(models.Model):
	"""Activities in the challenge. Category (e.g. letter) and owner only are mandatory."""
	challenge_group = models.ForeignKey(ChallengeGroup, on_delete=models.CASCADE)
	owner = models.ForeignKey(Member, on_delete=models.CASCADE)
	activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
	category = models.CharField(max_length=50)
	details = models.CharField(max_length=200, blank=True, default='')
	date_unlocked = models.DateTimeField(auto_now_add=True)
	date_completed = models.DateField(null=True, blank=True)
	
	class Meta:
		verbose_name_plural = 'activities'

	def __str__(self):
		"""Return a string representation of the model."""
		return (self.category + ' - ' + self.details)


