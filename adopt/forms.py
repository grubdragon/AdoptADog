from django import forms
from django.contrib.auth.models import User
from models import DogsUploaded,Dog
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

class DogForm(forms.ModelForm):
    

    class Meta:
        model = DogsUploaded
        exclude = ['uploader', 'dog']

    