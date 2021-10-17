from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from housing_app.models import Property

# Create your views here.

class PropertiesListView(ListView):
    model = Property

class PropertiesDetailView(DetailView):
    model = Property

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['review_list'] = Review.objects.all()
    #     return context
