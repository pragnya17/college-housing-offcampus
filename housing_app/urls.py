from django.urls import include, path
from django.contrib import admin

app_name = 'housing_app'
urlpatterns = [
    path('properties/', include('properties.urls')),
    path('admin/', admin.site.urls),
]