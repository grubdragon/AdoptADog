# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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
