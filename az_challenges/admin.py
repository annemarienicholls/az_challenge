from django.contrib import admin

from az_challenges.models import ChallengeGroup, Member, Activity

admin.site.register(ChallengeGroup)
admin.site.register(Member)
admin.site.register(Activity)
