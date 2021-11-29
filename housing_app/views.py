from django.shortcuts import get_object_or_404, render, HttpResponse, redirect 

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
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
        context = super(PropertiesDetailView, self).get_context_data(**kwargs)

        #try:
            # Sourced from https://www.valentinog.com/blog/detail/
            # get property object's title and find all the matchin ratings for that property
        property_id = self.kwargs.get("object").get("id")
        ratings = Rating.objects.filter(property_id=property_id)
        len_ratings = len(ratings)
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

        # except:
        #     # no ratings available yet
        #     avg_amenities = -1
        #     avg_service = -1
        #     avg_noise = -1

        context['property_id'] = property_id
        context['avg_amenities'] = avg_amenities
        context['avg_service'] = avg_service
        context['avg_noise'] = avg_noise

        return context


def myDash(request):
    model = Property.objects.all()
    return render(request, "properties/dashboard.html", {'model': model})


def map(request):
    model = Property.objects.all()
    return render(request, "map.html", {'model':model})

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
            # form = RatingForm(request.POST)
            #if form.is_valid():
            obj = Rating()
            obj.property_id= request.POST.get('property','')
            obj.amenities_rating = request.POST.get('amenities','')
            obj.services_rating = request.POST.get('services','')
            obj.noise_level_rating = request.POST.get('noise','')
            obj.save()
            return HttpResponseRedirect('/properties/rating')
        # else:
            # form = RatingForm()
        return render(request, 'properties/rating.html', {'properties': Property.objects.all()})


