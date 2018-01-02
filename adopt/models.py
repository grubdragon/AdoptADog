# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Dog(models.Model):

    breed = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"

    def __str__(self):
        return self.breed

class UserProfile(models.Model):

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
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
    image_link = models.URLField()


    class Meta:
        verbose_name = "DogsUploaded"
        verbose_name_plural = "DogsUploadeds"

    def __str__(self):
        return self.name
    
    
    
