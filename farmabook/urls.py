from django.urls import path
from . import views

#! New

urlpatterns = [
    path('', views.post_list, name='post_list'),
]