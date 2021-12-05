from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages

# REFERENCES
# Title: How to make add replies to comments in django
# Date accessed: 11/26/2021
# Date created: 7/2017
# Link: https://stackoverflow.com/questions/44837733/how-to-make-add-replies-to-comments-in-django

# Title: Create a Discussion Forum in Python Django
# Date accessed: 11/21/21
# Author: Project Gurukul
# Link: https://projectgurukul.org/python-django-online-discussion-forum/

# Title: Django Messages Framework
# Date accessed: 12/1/2021
# Date created: 6/2/2020
# Author: Jaysha from Ordinary Coders
# Link: https://ordinarycoders.com/blog/article/django-messages-framework

# Title: Create a Discussion Forum
# Date accessed: 11/9/2021
# Author: Data Flair
# Link: https://data-flair.training/blogs/discussion-forum-python-django/

# Title: Django - Taking values from POST request
# Date accessed: 11/15/21
# Date created: 7/2012
# Link: https://stackoverflow.com/questions/11336548/django-taking-values-from-post-request/11336580

def forumHome(request):
    forums=myForum.objects.all()
    count=forums.count()
    myDiscussions = Discussion.objects.all()

    form = CreateInDiscussion()
    if request.method == 'POST':
        request.Get_Mutable = True
        print(request.POST.get('forum', ''))
        print(request.POST.get('discuss', ''))
        print(request.POST.get('name', ''))
        
        form = CreateInDiscussion()
        form = CreateInDiscussion(request.POST)
        form.data = form.data.copy()
        form.data['myForum'] = request.POST.get('forum', '')
        form.data['discuss'] = request.POST.get('discuss', '')
        form.data['name'] = request.POST.get('name', '')
        print("After seting the form fields")
        #print(form)

        if form.is_valid():
            form.save()
            return redirect('/forum')
        else:
            messages.warning(request, "Reply not created! You CANNOT have only white space in any of the fields.")
            return redirect('/forum')
    context={'forums':forums,
              'count':count,
              'myDiscussions':myDiscussions,
              'form':form}
    return render(request, 'forum/forum.html', context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        print(request.POST)
        form = CreateInForum(request.POST)
        form.topic = request.POST.get('topic','')
        form.description = request.POST.get('description','')
        form.name = request.POST.get('name','')
        print("Before if statement")
        if form.is_valid():
            print("After if statement")
            form.save()
            return redirect('/forum')
    context ={'form':form}
    return render(request,'forum/addInForum.html',context)
