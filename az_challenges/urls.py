"""Defines URL patterns for az_challenges."""

from django.urls import path

from . import views

app_name = 'az_challenges'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show all Challenge Groups
    path('challenges/', views.challenges, name='challenges'),
    
    # Detail page for a single Challenge
    path('challenges/<int:challenge_id>/', views.challenge, name='challenge'),
    
    # Page for adding new Challenge
    path('new_challenge/', views.new_challenge, name='new_challenge'),
    
    # Page for adding a new member.
    path('new_member/<int:challenge_id>/', views.new_member, name='new_member'),
    
]
