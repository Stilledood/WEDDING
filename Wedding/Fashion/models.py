from django.db import models
from django.shortcuts import redirect ,render, reverse
from MainApp.models import CLientDetails
from multiselectfield import MultiSelectField


class Clothing(CLientDetails):
    '''Class to define a model for all cloth designers'''

    type_of_services = (
        ('Rochii Mireasa','Rochii Mireasa'),
        ('Rochii de seara' , 'Rochii de seara'),
        ('Costume barbati' , 'Costume barbati'),
        ('Incaltime dama', 'Incaltaminte dama'),
        ('Incaltaminte barbati', 'Incaltaminte barbati'),
        ('Haine copii', 'Haine copii')
    )

    servicii = MultiSelectField(choices=type_of_services,default='')
    facilities = (
        ('Haine comanda','Haine comanda'),
        ('Personalizare/Retusare','Personalizare/Retusare')
    )

    facilitati = MultiSelectField(choices=facilities,default='')


    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('clothing_details',kwargs={'pk':self.pk})


class Jewelerry(CLientDetails):
    '''Class to define a model for all jewelley makers and accesories'''

    services_provided = (
        ('Verighete', 'Verighete'),
        ('Alte bijuterii', 'Alte bijuterii')
    )

    servicii = MultiSelectField(choices=services_provided, default='')

    facilities = (
        ('Bijuterii la comanda', 'Bijuterii la comanda'),
        ('Modificare bijuterii', 'Modificare bijuterii'),
        ('Buyback', 'Buyback')
    )

    facilitati = MultiSelectField(choices=facilities,default='')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('jewellery_details',kwargs={'pk':self.pk})



class MagazinAccesorii(CLientDetails):
    '''Class to construct a model for all accesories sellers'''

    services_type = (
        ('Accesorii nunta','Accesorii nunta'),
        ('Accesorii botez', 'Accesorii botez'),
        ('Invitatii', 'Invitatii'),
        ('Accesorii petreceri', 'Accesorii petreceri')
    )

    servicii = MultiSelectField(choices=services_type,default='')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('accesories_details', kwargs={'pk':self.pk})





