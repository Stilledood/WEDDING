import os
from django.db import models
from django.shortcuts import reverse,render,redirect
from multiselectfield import MultiSelectField
from ..MainApp.models import CLientDetails


class Music(CLientDetails):
    '''Class to create a model for all music part'''


    formation_type = (
        ('Formatie','Formatie'),
        ('DJ','DJ')
    )

    musical_styles = (
        ('Clasic','Clasic'),
        ('Disco','Disco'),
        ('Folclor','Folclor'),
        ('Hip-Hop','Hip=Hop'),
        ('Instrumental','Instrumental'),
        ('Jazz','Jazz'),
        ('Latino','Latino'),
        ('Pop','Pop'),
        ('Rock','Rock'),
    )

    muscial_styles_field = MultiSelectField(choices=musical_styles,default='')
    tip = models.CharField(choices=formation_type,default='')
    name = models.CharField(max_length=200,default='')
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    county = models.CharField(choices=zip(romanian_cities.keys(), romanian_cities.keys()), default='Bucuresti')
    city = models.CharField(max_length=255, choices=city_choices, default='Bucuresti')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detalii_muzica',kwargs={'id':self.pk})

    def get_update_url(self):
        return reverse('update_muzica',kwargs={'id':self.pk})
