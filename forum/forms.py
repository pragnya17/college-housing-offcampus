from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    class Meta:
        model= myForum
        fields = "__all__"

class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"
        labels = {
            'myForum': ('Discussion topic'),
            'discuss': ('Your reply'),
        }
