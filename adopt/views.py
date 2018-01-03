# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import UserProfile, Dog, DogsUploaded
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def upload(request):

    if request.method == 'GET':
        return render(request,'upload.html')

    if request.method == 'POST':
        name = request.POST['name']
        # Handle other data similarly
        return render(request, 'thankyou.html')

@csrf_protect
def display_dogs(request):

    if request.method == 'POST':
        breed = request.POST['breed']
        print breed
        dogs = DogsUploaded.objects.filter(dog__lookup_breed__iexact=breed)
        return render(request,'dogs.html',{ 'dogs':dogs })

    if request.method == 'GET':
        return render(request, 'enter_breed.html')
def single_dog(request,pk):

    dog = DogsUploaded(pk=pk)
    return render(request,'single_dog.html',{ 'dog': dog})

