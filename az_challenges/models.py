from django.db import models

class ChallengeGroup(models.Model):
	"""Links people with activities for a single challenge"""
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
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
