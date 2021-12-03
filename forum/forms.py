from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    class Meta:
        model= myForum
        fields = "__all__"
        labels = {
            'name': ('Posting As:'),
            'topic': ('Title of your post'),
            'description': ('Body of your post'),
        }

class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"
        labels = {
            'myForum': ('Discussion topic'),
            'discuss': ('Your reply'),
            'name': ('Posting As:'),
        }
