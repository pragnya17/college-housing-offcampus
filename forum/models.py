from django.db import models

# Create your models here.

from django.db import models 
    
#parent model
class myForum(models.Model):
    name=models.CharField(max_length=200,default="anonymous")
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 
#child model
class Discussion(models.Model):
    myForum = models.ForeignKey(myForum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    name = models.CharField(max_length=200,default="anonymous")
    date_created = models.DateTimeField(auto_now_add=True,null=True)
 
    def __str__(self):
        return str(self.discuss)
