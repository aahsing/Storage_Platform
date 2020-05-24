from django.urls import path
from . import views

urlpatterns = [
    path('browse', views.index, name='index'),
    path('createdir', views.createdir, name='createdir'),
    path('quota', views.quota, name='quota'),
]