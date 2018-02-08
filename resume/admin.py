from django.contrib import admin

from .models import Resume, Career, Education


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone_number', 'about_me', 'created_at']
        

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['resume', 'since', 'until', 'currently_employed', 'company', 'position']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['resume', 'since', 'until', 'currently_attending', 'school_name', 'major', 'research_content']
