from django.urls import path
from django.views.generic import TemplateView

app_name = 'housing_app'
urlpatterns = [
    path('map/', TemplateView.as_view(template_name="map.html"), name="map")
from django.urls import include, path
from django.contrib import admin

app_name = 'housing_app'
urlpatterns = [
    path('properties/', include('properties.urls')),
    path('admin/', admin.site.urls),
]