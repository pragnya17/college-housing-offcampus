from django.shortcuts import get_object_or_404, render, HttpResponse, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
from .models import *
from .filters import PropertyFilter
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class PropertiesListView(ListView):
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PropertyFilter(self.request.GET, queryset=self.get_queryset())
        return context


# Code sourced from https://stackoverflow.com/questions/51950416/reversemanytoonedescriptor-object-has-no-attribute-all
class PropertiesDetailView(DetailView):
    model = Property

    def get_context_data(self, **kwargs):
        context = super(PropertiesDetailView, self).get_context_data(**kwargs)

        # Sourced from https://www.valentinog.com/blog/detail/
        # get property object's title and find all the matchin ratings for that property

        property_id = kwargs.get("object").id
        reviews = Review.objects.filter(property_id=property_id)
        len_reviews = len(reviews)
        if len_reviews > 0:
            overall_sum = 0
            amenities_sum = 0
            service_sum = 0
            noise_sum = 0
            text_reviews_and_bias = {}
            for review in reviews:
                overall_sum += review.overall_rating
                amenities_sum += review.amenities_rating
                service_sum += review.services_rating
                noise_sum += review.noise_level_rating
                text_reviews_and_bias[review.text_review] = review.biased_review
            avg_overall = overall_sum/len_reviews    
            avg_amenities = amenities_sum / len_reviews
            avg_service = service_sum / len_reviews
            avg_noise = noise_sum / len_reviews
        else:
        # no ratings available yet
            avg_overall = -1
            avg_amenities = -1
            avg_service = -1
            avg_noise = -1
            text_reviews_and_bias = []

        context['avg_overall'] = round(avg_overall, 2)
        context['avg_amenities'] = round(avg_amenities, 2)
        context['avg_service'] = round(avg_service, 2)
        context['avg_noise'] = round(avg_noise, 2)
        context['text_reviews_and_bias'] = text_reviews_and_bias

        return context


def myDash(request):
    model = Property.objects.all()
    return render(request, "properties/dashboard.html", {'model': model})


def map(request):
    model = Property.objects.all()
    return render(request, "map.html", {'model':model})


def index(request):
    if request.user.is_authenticated:
        favorited = request.user.fav_properties.all()
        return render(request, "index.html", {'favorited':favorited})
    else:
        return render(request, "index.html")

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['review_list'] = Review.objects.all()
    #     return context

def ReviewFormView(request):
    if request.method == 'POST':
        obj = Review()
        obj.property_id= request.POST.get('property','')
        obj.overall_rating = request.POST.get('overall','')
        obj.amenities_rating = request.POST.get('amenities','')
        obj.services_rating = request.POST.get('services','')
        obj.noise_level_rating = request.POST.get('noise','')
        obj.text_review = request.POST.get('text_review', '')
        obj.save()
        messages.success(request, "Your review was submitted!")
        return HttpResponseRedirect('/review')
    return render(request, 'properties/review.html', {'properties': Property.objects.all()})

@login_required
def favorite_property(request, fav_id):
    property = get_object_or_404(Property, id=fav_id)
    user = request.user
    if request.method == 'POST':
        property.favorite.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def unfavorite_property(request, fav_id):
    property = get_object_or_404(Property, id=fav_id)
    user = request.user
    if request.method == 'POST':
        property.favorite.remove(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))