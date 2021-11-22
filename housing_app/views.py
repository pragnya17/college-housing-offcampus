from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect 

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from housing_app.models import Property
from . import models
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from housing_app.models import RatingForm
from .models import *
from .filters import PropertyFilter


class PropertiesListView(ListView):
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PropertyFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def favorite_property(request):
        model = Property.objects.all()
        if (request.method == "POST"):
            # print(request.POST.get("property", ""))
            myProperty = get_object_or_404(Property, pk=request.POST.get("property", ""))
            if myProperty.favorite:
                myProperty.favorite = False
            else:
                myProperty.favorite = True
            myProperty.save()
        return render(request, "properties/properties.html", {'model': model})


# Code sourced from https://stackoverflow.com/questions/51950416/reversemanytoonedescriptor-object-has-no-attribute-all
class PropertiesDetailView(DetailView):
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ratings = self.object.ratings.all()

        # get average ratings in each category
        len_ratings = len(ratings)
        if len_ratings == 0:  # no ratings available yet
            avg_amenities = -1
            avg_service = -1
            avg_noise = -1
        else:
            amenities_sum = 0
            service_sum = 0
            noise_sum = 0
            for rating in ratings:
                amenities_sum += rating.amenities_rating
                service_sum += rating.services_rating
                noise_sum += rating.noise_level_rating
            avg_amenities = amenities_sum / len_ratings
            avg_service = service_sum / len_ratings
            avg_noise = noise_sum / len_ratings

        context['avg_amenities'] = avg_amenities
        context['avg_service'] = avg_service
        context['avg_noise'] = avg_noise

        return context


def myDash(request):
    model = Property.objects.all()
    return render(request, "properties/dashboard.html", {'model': model})


def index(request):
    model = Property.objects.all()
    return render(request, "index.html", {'model':model})

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['review_list'] = Review.objects.all()
    #     return context

def RatingFormView(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            obj = Rating()
            obj.amenities_rating = form.cleaned_data['amenities_rating']
            obj.services_rating = form.cleaned_data['services_rating']
            obj.noise_level_rating = form.cleaned_data['noise_level_rating']
            obj.save()
            return HttpResponseRedirect('/properties/rating')
    else:
        form = RatingForm()

    return render(request, 'properties/rating.html', {'form': form})

