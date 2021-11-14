# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from housing_app.models import Property
from . import models

# Create your views here.

class PropertiesListView(ListView):
    model = Property

class PropertiesDetailView(DetailView):
    model = Property

def reviews_list(request):
    reviews_list = models.Review.objects.all()
    return render(request, 'templates', {'reviews_list': reviews_list})

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['review_list'] = Review.objects.all()
    #     return context

def ReviewFormView(request):
    if request.method == 'POST':
        form = models.ReviewForm(request.POST)
        if form.is_valid():
            obj = models.Review()
            obj.amenities = form.cleaned_data['amenities_rating']
            obj.management = form.cleaned_data['management']
            obj.noise_level = form.cleaned_data['noise_level']
            obj.save()
            return HttpResponseRedirect('/properties/review')
    else:
        form = models.ReviewForm()

    return render(request, 'properties/review.html', {'form': form})

