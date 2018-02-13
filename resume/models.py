from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.core.validators import RegexValidator

import re

# v 0.1.0 (Wanted style)
class Resume(models.Model):
    # essential fields
    title = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14, validators=[
        RegexValidator(r'^01[016789]-[2-9]\d{2,3}-\d{4}$', message='Enter a valid phone number'),
    ])
    about_me = models.TextField()
    # auto fields
    created_at = models.DateTimeField(auto_now_add=True)
    # Relational model: User
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Career(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    since = models.DateField()
    until = models.DateField(blank=True, null=True)
    currently_employed = models.BooleanField()
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    achievement = models.TextField()
    
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    since = models.DateField()
    until = models.DateField(blank=True, null=True)
    currently_attending = models.BooleanField()
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    research_content = models.TextField()

class Award(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    at = models.DateField()
    activity_name = models.CharField(max_length=50)
    detail = models.TextField()

class Link(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    github = models.CharField(max_length=50, blank=True) # id
    stackoverflow = models.URLField(blank=True, validators=[ # url 
        RegexValidator(r'^(https?:\/\/)?stackoverflow\.com\/users\/\d+\/\w+\/?$', 
            message='Stackoverflow link should be "https://stackoverflow.com/users/<your_id>/<username>/" format')
    ]) 
    linkedin = models.URLField(blank=True, validators=[ # url
        RegexValidator(r'^(https?:\/\/)?www\.linkedin\.com\/in\/\w+\/?$', 
            message='Linkedin link should be "https://www.linkedin.com/in/<your_id>/" format')
    ]) 
    facebook = models.CharField(max_length=50, blank=True) # id
    twitter = models.CharField(max_length=50, blank=True, validators=[
        RegexValidator(r'[^@a-zA-Z0-9_]+', message='Enter a valid twitter ID, except leading @')
        ]) # id (except @)
    google_plus = models.URLField(blank=True, validators=[
        RegexValidator(r'^(https?:\/\/)?plus\.google\.com\/w+\/?$', 
            message='Google+ link should be "https://plus.google.com/<your_id>/" format')
    ]) 
    blog = models.URLField(blank=True)
