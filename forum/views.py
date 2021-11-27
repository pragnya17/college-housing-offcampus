from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.core.exceptions import ValidationError

# Create your views here.

#def forumHome(request):
#    return render(request, 'forum/forum.html')

def forumHome(request):
    forums=myForum.objects.all()
    count=forums.count()
    #discussions=[]
    myDiscussions = Discussion.objects.all()
    context={'forums':forums,
              'count':count,
              'myDiscussions':myDiscussions}
    return render(request, 'forum/forum.html', context)
    #return HttpResponseRedirect(request,'forum:forum.html',context)
    #return HttpResponseRedirect(reverse('forum:addInForum'))

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context ={'form':form}
    return render(request,'forum/addInForum.html',context)
    #return render(request, 'forum/templates/forum/addInForum.html' ,context)
    #return render(request, 'housing/properties.html', context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context ={'form':form}
    return render(request,'forum/addInDiscussion.html',context)
