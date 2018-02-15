from django.urls import path

from . import views


app_name = 'resume'

urlpatterns = [
    path('list/', views.resume_list, name='list'),
    path('new', views.resume_form, name='form'),
]
