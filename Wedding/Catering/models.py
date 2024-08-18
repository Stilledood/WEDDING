from django.db import models
from django.shortcuts import render,reverse, redirect



class Cofetarie(models.Model):
    '''Class to define a model for all pastryshops'''

    name = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    meniu = models.FileField(upload_to='pdf-menus')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cofetarie_details',kwargs={'pk':self.pk})



    


