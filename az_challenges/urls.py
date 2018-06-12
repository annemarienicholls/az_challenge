"""Defines URL patterns for az_challenges."""

from django.urls import path

from . import views

app_name = 'az_challenges'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show all Challenge Groups
    path('challenges/', views.challenges, name='challenges'),
    

]
