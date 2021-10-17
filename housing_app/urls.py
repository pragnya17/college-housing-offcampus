from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin

app_name = 'housing_app'
urlpatterns = [
    path('map/', TemplateView.as_view(template_name="map.html"), name="map"),
    #path('properties/', include('properties.urls')),
    path('admin/', admin.site.urls),
]
