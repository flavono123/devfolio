from django.db import models
from django.contrib.auth import get_user_model


# v 0.1.0 (Wanted style)
class Resume(models.Model):
    # essential fields
    name = models.CharField(max_length=25)
    base_info = models.TextField()
    # auto fields
    created_at = models.DateTimeField(auto_now_add=True)
    # Relational model: User
    User = get_user_model()
    superuser = User.objects.get(username='flavono123')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             default=superuser.id)

    def __str__(self):
        return self.name

class Career(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    since = models.DateField()
    until = models.DateField(blank=True, null=True)
    currently_employed = models.BooleanField()
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    achivement = models.TextField(default='')
    
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    research_content = models.TextField()
    since = models.DateField()
    until = models.DateField(blank=True)
    currently_attending = models.BooleanField()

class Award(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=50)
    detail = models.TextField()
    at = models.DateField()

class Link(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    email = models.EmailField()
    github = models.CharField(max_length=50, blank=True)
    stackoverflow = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    google_plus = models.CharField(max_length=50, blank=True)
    blog = models.URLField(blank=True)
