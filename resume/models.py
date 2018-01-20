from django.db import models


# v 0.1.0 (Wanted style)
class Resume(models.Model):
    # essential fields
    name = models.CharField(max_length=25)
    base_info = models.TextField()
    # optional fields
    career = models.TextField(blank=True)
    education = models.TextField(blank=True)
    award = models.TextField(blank=True)
    language = models.TextField(blank=True)
    link = models.TextField(blank=True)
