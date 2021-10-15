from django.contrib import admin
from django.urls import path, include, reverse

app_name = 'housing_app'
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]