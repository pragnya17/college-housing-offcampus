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
from housing_app.models import ReviewForm
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

class PropertiesDetailView(DetailView):
    model = Property

def reviews_list(request):
    reviews_list = models.Review.objects.all()
    return render(request, 'templates', {'reviews_list': reviews_list})

def myDash(request):
    model = Property.objects.all()
    return render(request, "properties/dashboard.html", {'model':model})

def index(request):
    model = Property.objects.all()
    return render(request, "index.html", {'model':model})

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['review_list'] = Review.objects.all()
    #     return context

def ReviewFormView(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = models.Review()
            obj.review_title = form.cleaned_data['review_title']
            obj.amenities = form.cleaned_data['amenities_rating']
            obj.management = form.cleaned_data['management']
            obj.noise_level = form.cleaned_data['noise_level']
            obj.save()
            return HttpResponseRedirect('/properties/review')
    else:
        form = ReviewForm()

    return render(request, 'properties/review.html', {'form': form})

