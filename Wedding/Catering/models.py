from django.db import models
from django.shortcuts import render,reverse, redirect
from multiselectfield import MultiSelectField
from ..MainApp.models import CLientDetails


class Cofetarie(CLientDetails):
    '''Class to define a model for all pastryshops'''

    meniu = models.FileField(upload_to='pdf-menus')
    servicii = (
        ('Candy Bar','Candy Bar'),
        ('Torturi personalizate','Torturi personalizate'),
        ('Livrare','Livrare'),

    )
    servicii_cofetarie = MultiSelectField(choices=servicii,default='')


    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('cofetarie_details',kwargs={'pk':self.pk})



class Catering(CLientDetails):
    '''Class to define a model for food catering clients'''


    meniu = models.FileField(upload_to='pdf-menus')


    servicii = (
        ('Bar si bauturi', 'Bar si bauturi'),
        ('Bufet', 'Bufet'),
        ('CandyBar','CandyBar'),
        ('Chef','Chef'),
        ('Degustare','Degustare'),
        ('Livrare','Livrare'),
        ('Aranjare','Aranjare'),
        ('Personal Servire','Personal Servire'),
    )

    servicii_catering = MultiSelectField(choices=servicii,default='')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('catering_details',kwargs={'pk':self.pk})


