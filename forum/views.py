from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse  
from .models import * 
from .forms import * 

# Create your views here.

#def forumHome(request):
#    return render(request, 'forum/forum.html')

def forumHome(request):
    forums=myForum.objects.all()
    count=forums.count()
    #discussions=[]
    myDiscussions = Discussion.objects.all()
    #for i in forums:
        #discussion_set = Discussion.objects.filter(i=i)
        #reply = Discussion.objects.filter(i=i)

        #discussions.append(i.discussion_set.all())
        #discussions.append(discussion_set)
        #discussions.append(i.name)

        #discussions.append(i.reply.all())
        

        #post = Post.objects.filter(id=myid).first()
        #replies = Replie.objects.filter(post=post)
 
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