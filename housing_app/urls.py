"""housing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views., name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
# adapted from https://testdriven.io/blog/django-social-auth/
from housing_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    #path('properties/<int:pk>/', views.PropertiesDetailView, name='property'),
    #path('properties/', views.favorite_property, name = 'properties'),
    #path('dashboard', views.DashboardListView.as_view(template_name="properties/dashboard.html"), name = "dashboard"), 
    path('dashboard', views.myDash, name="dashboard"),
    path('forum/', include('forum.urls')),
    path('properties/rating', views.RatingFormView, name='rating'),

]
