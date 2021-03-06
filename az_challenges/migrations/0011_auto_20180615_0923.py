# Generated by Django 2.0.6 on 2018-06-15 08:23

from django.db import migrations
import string

def activity_type_initial(apps, schema_editor):
	# ref https://docs.djangoproject.com/en/2.0/topics/migrations/#data-migrations
	ActivityType = apps.get_model('az_challenges', 'ActivityType')
	ChallengeType = apps.get_model('az_challenges', 'ChallengeType')
	
	
	#Create A-Z activities for the A-Z challenge type
	challenge_type_az = ChallengeType.objects.get(id=1)
	
	for s in string.ascii_uppercase:
		new_activity_type = ActivityType()
		new_activity_type.name = s
		new_activity_type.challenge_type = challenge_type_az
		new_activity_type.save()
	
	#Create custom activity for the Custom challenge type
	challenge_type_custom = ChallengeType.objects.get(id=2)
	
	custom_activity_type = ActivityType()
	custom_activity_type.name = 'Custom'
	custom_activity_type.challenge_type = challenge_type_custom
	custom_activity_type.save()
	

class Migration(migrations.Migration):

    dependencies = [
        ('az_challenges', '0010_activitytype'),
    ]

    operations = [
		migrations.RunPython(activity_type_initial),
    ]
