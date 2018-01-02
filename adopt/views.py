# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import UserProfile, Dog, DogsUploaded

# Create your views here.
def index(request):
    render(request,'index.html')

def home(request):
    render(request,'home.html')

def upload(request):

    if request.method == 'GET':
        render(request,'upload.html')

    if request.method == 'POST':
        name = request.POST['name']
        # Handle other data similarly
        render(request, 'thankyou.html')

def display_dogs(request,breed):

    dogs = DogsUploaded(dog__lookup_breed__iexact=breed)
    render(request,'dogs.html',{ 'dogs':dogs })

def single_dog(request,pk):

    dog = DogsUploaded(pk=pk)
    render(request,'single_dog.html',{ 'dog': dog})

