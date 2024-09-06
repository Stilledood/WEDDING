from django.db import models
from django.shortcuts import render,reverse, redirect
from multiselectfield import MultiSelectField


class Cofetarie(models.Model):
    '''Class to define a model for all pastryshops'''

    name = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    meniu = models.FileField(upload_to='pdf-menus')
    servicii = (
        ('Candy Bar','Candy Bar'),
        ('Torturi personalizate','Torturi personalizate'),
        ('Livrare','Livrare'),

    )
    servicii_cofetarie = MultiSelectField(choices=servicii,default='')
    instagram_page = models.URLField()
    tik_tok_page = models.URLField()
    facebook_page = models.URLField()
    website_page = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cofetarie_details',kwargs={'pk':self.pk})



class Catering(models.Model):
    '''Class to define a model for food catering clients'''

    name = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    meniu = models.FileField(upload_to='pdf-menus')
    instagram_page = models.URLField()
    tik_tok_page = models.URLField()
    facebook_page = models.URLField()
    website_page = models.URLField()

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
        return self.name

    def get_absolute_url(self):
        return reverse('catering_details',kwargs={'pk':self.pk})


