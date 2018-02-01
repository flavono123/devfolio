from django.contrib import admin

from .models import Resume, Career


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_info', 'created_at']
        

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['resume', 'since', 'until', 'currently_employed', 'company', 'position']
