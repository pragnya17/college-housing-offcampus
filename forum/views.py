from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

#def forumHome(request):
#    return render(request, 'forum/forum.html')

def forumHome(request):
    forums=myForum.objects.all()
    count=forums.count()
    #discussions=[]
    myDiscussions = Discussion.objects.all()


    #discuss = request.POST.get('Reply', False)
    #name = request.POST.get('Name', False)
    #specificForumID = request.POST.get('forum')
    #x = myForum.objects.get(name=request.POST.get('forum', False))
    #form = Discussion(myForum = x, discuss = discuss, name = name)
    form = CreateInDiscussion()
    if request.method == 'POST':
        request.Get_Mutable = True
        print(request.POST.get('forum', ''))
        print(request.POST.get('discuss', ''))
        print(request.POST.get('name', ''))
        #hereForum = request.POST[2]
        #print(request.POST['myForum.forum'])
        #theName = request.POST.get('name', False)  # ask the user for this in case they want to change their name to Ananymous # good
        #theDiscuss = request.POST.get('discuss', False) # ask the user for this  # good
        #theRightForum = request.POST.get('myForum', False)   # don't ask the user for this
        #form = CreateInDiscussion(discuss = theDiscuss, name = theName, myForum = theRightForum)
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
    #return HttpResponseRedirect(request,'forum:forum.html',context)
    #return HttpResponseRedirect(reverse('forum:addInForum'))

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        print(request.POST)
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context ={'form':form}
    return render(request,'forum/addInForum.html',context)
    #return render(request, 'forum/templates/forum/addInForum.html' ,context)
    #return render(request, 'housing/properties.html', context)

#def addInDiscussion(request):
    ##form = CreateInDiscussion()
    #discuss = request.POST.get('Reply', False)
    #name = request.POST.get('Name', False)
    #x = myForum.objects.get(name=request.POST.get('forum', False))

    #form = Discussion(myForum = x, discuss = discuss, name = name)
    #form.save()
    #context = {'form':form}
    #return render(request,'forum/addInDiscussion.html', context)
