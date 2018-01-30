from django.db import models


# v 0.1.0 (Wanted style)
class Resume(models.Model):
    # essential fields
    name = models.CharField(max_length=25)
    base_info = models.TextField()
    # optional fields
    education = models.TextField(blank=True)
    award = models.TextField(blank=True)
    link = models.TextField(blank=True)
    # auto fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Career(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    since = models.DateField()
    until = models.DateField(blank=True)
    currently_employed = models.BooleanField()
    
