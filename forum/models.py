from django.db import models

# Create your models here.

from django.db import models

#parent model
class myForum(models.Model):
    topic= models.CharField(max_length=300)
    description = models.TextField()
    name=models.CharField(max_length=200)

    def __str__(self):
        return str(self.topic)

#child model
class Discussion(models.Model):
    myForum = models.ForeignKey(myForum,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.discuss)
