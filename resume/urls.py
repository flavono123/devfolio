from django.urls import path

from . import views


app_name = 'resume'

urlpatterns = [
    path('list/', views.resume_list, name='list'),
    path('new', views.resume_form, name='form'),
    
    
    path('career/new', views.career_form, name='career_form'),
    path('education/new', views.education_form, name='education_form'),
    path('award/new', views.award_form, name='award_form'),
    path('link/new', views.link_form, name='link_form'),
]
