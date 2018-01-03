# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Dog(models.Model):

    # lookup_breed = 'GermanShepherd'
    # breed = 'German Shepherd'
    lookup_breed = models.CharField(max_length=30, default='')
    breed = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"

    def __str__(self):
        return self.breed

    def clean():
        self.lookup_breed = self.breed.replace(' ','')


class UserProfile(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    dogs_adopted = models.ForeignKey(Dog, related_name='dogs_adopted', on_delete=models.CASCADE)
    dogs_putup = models.ForeignKey(Dog, related_name='dogs_putup', on_delete=models.CASCADE)
    rating = models.FloatField()

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"

    def __str__(self):
        return  self.name

class DogsUploaded(models.Model):

    name = models.CharField(max_length=20, blank=True)
    uploader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    image = models.FileField(upload_to='uploads/')
    description = models.CharField(max_length=200, default='')


    class Meta:
        verbose_name = "DogsUploaded"
        verbose_name_plural = "DogsUploadeds"

    def __str__(self):
        return self.name
    
    
    
