from django.db.models import fields
from django.forms import ModelForm
from .models import *

class addTech(ModelForm):
    class Meta:
        model=AddTech
        fields = ['name','price']
        