from django.urls import path
from django.contrib import admin
from . import views


app_name = "forum"
urlpatterns = [
    path('', views.forumHome, name = "forum_home"), 
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
]