from django.urls import path

from . import views


app_name = 'resume'

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('list/', views.list, name='list'),
]
