from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin
from forum import views 
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
# adapted from https://testdriven.io/blog/django-social-auth/
from housing_app import views

app_name = 'housing_app'
urlpatterns = [
    path('', include('housing_app.urls')),
    path('properties/', views.PropertiesListView.as_view(template_name="properties/properties.html"), name='properties'),
    path('properties/<int:pk>/', views.PropertiesDetailView.as_view(template_name="properties/property.html"), name='property'),
    path('map/', TemplateView.as_view(template_name="map.html"), name="map"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
