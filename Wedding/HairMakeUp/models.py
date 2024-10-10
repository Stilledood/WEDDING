from django.db import models
from django.shortcuts import  redirect,reverse
from multiselectfield import MultiSelectField
from MainApp.models import CLientDetails


class MakeUpSaloon(CLientDetails):
    '''Class to construct a model for makeup saloons'''
    tip_servicii = (
        ('Hair Saloon', 'Hair Saloon'),
        ('Make Up', 'Make Up')
    )
    servicii_select = MultiSelectField(choices=tip_servicii, default='')
    servicies_hair_makeup = (
        ('Accesorii Par','Accesorii Par'),
        ('Bronzare','Bronzare'),
        ('Extensii Par','Extensii Par'),
        ('Extensii Gene', 'Extensii Gene'),
        ('Manichiura / Pedichiura', 'Manichiura / Pedichiura'),
        ('Frizerie / Barber Shop', 'Frizerie / Barber Shop'),
        ('Coafor', 'Coafor'),
        ('Epilare', 'Epilare'),

    )

    servicies_field = MultiSelectField(choices=servicies_hair_makeup,default='')
    location_available = (
        ('Salon', 'Salon'),
        ('La domiciliu clientului', 'La domiciliu clientului')
    )

    locatie_desfasurare = MultiSelectField(choices=location_available,default='')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('makeup_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('makeup_update',kwargs={'pk':self.pk})


