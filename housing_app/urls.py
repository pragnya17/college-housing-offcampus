from django.urls import path
from django.views.generic import TemplateView

app_name = 'housing_app'
urlpatterns = [
    path('map/', TemplateView.as_view(template_name="map.html"), name="map")
]