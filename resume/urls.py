from django.urls import path

from . import views


app_name = 'resume'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('list/', views.resume_list, name='list'),
    
    
    path('career/new', views.career_form, name='career_form'),
]
