import os
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.deconstruct import deconstructible
from django.shortcuts import reverse,render,redirect
from multiselectfield import MultiSelectField
from ..MainApp.models import CLientDetails




class BallRoom(CLientDetails):
    """Class to construct a model for all ballrooms"""


    minimum_guests_number = models.IntegerField()
    maximum_guests_number = models.IntegerField()

    facillities = (
        ('Aer Conditionat', 'Aer Conditionat'),
        ('Sistem de sonorizare', 'Sistem de sonorizare'),
        ('Lumini arhitecturale', 'Lumini arhitecturale'),
        ('Iluminat profesional', 'Iluminat profesional'),
        ('Ring de dans', 'Ring de dans'),
        ('Scenă pentru formație/muzicieni', 'Scenă pentru formație/muzicieni'),
        ('Decoratiuni incluse', 'Decoratiuni incluse'),
        ('Baie Separata', 'Baie Separata'),
        ('Prezidiu', 'Prezidiu'),
        ('Decor mese', 'Decor mese'),
        ('Wifi', 'Wifi'),
        ('Decor scaune', 'Decor scaune'),
        ('Meniuri pentru meese', 'Meniuri pentru mese'),
        ('Vedere panoramica', 'Vedere panoramica'),
        ('Proximitea centrului orasului', 'Proximitatea centrului orasului'),
        ('Foto corner', 'Foto corner'),
        ('Casuta de dar', 'Casuta de dar'),
        ('Locatie pe lac', 'Locatie pe lac'),
        ('Vedere la lac', 'Vedere la lac'),
        ('Locatie in padure', 'Locatie in padure'),
        ('Event planner', 'Event planner'),
        ('Stativ cu lista invitatilor', 'Stativ cu lista invitatilor'),
        ('Numere pentru mese', 'Numere pentru mese'),
        ('Loc de relaxare', 'Loc de relaxare '),
    )
    location_facilities = MultiSelectField(choices=facillities, default='')
    catering = (
        ('Bucatarie proprie', 'Bucatarie proprie'),
        ('Servicii de catering incluse sau opționale', 'Servicii de catering incluse sau opționale'),
        ('Meniuri speciale', 'Meniuri speciale'),
        ('Degustare meniu', 'Degustare meniu'),
        ('Serviciul ospatarilor gratuit', 'Serviciul ospatarilor gratuit'),
        ('Candy Bar', 'Candy Bar'),
        ('Shot Bar', 'Shot Bar'),
        ('Fruit Bar', 'Fruit Bar'),
        ('Cocktail Bar', 'Cocktail Bar'),
        ('Obiceiuri', 'Obiceiuri'),
        ('Open bar', 'Open bar'),
        ('All inclusive', 'All inclusive'),
        ('Cofetarie/Patiserie', 'Cofetarie/Patiserie '),
        ('Drum asfaltat', 'Drum asfaltat'),
    )
    catering_options = MultiSelectField(choices=catering, default='')
    parking = (
        ('Parcare gratuita', 'Parcare gratuita'),
        ('Parcare platita', 'Parcare platita'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Parcare iluminata', 'Parcare iluminata'),
    )
    parking_options = MultiSelectField(choices=parking, default='')
    zona_exterioara = (
        ('Loc pentru fumat', 'Loc pentru fumat'),
        ('Terasa acoperita', 'Terasa acoperita'),
        ('Terasa descoperita', 'Terasa descoperita'),
        ('Piscina', 'Piscina'),
        ('Foisor evenimente', 'Foisor evenimente'),
        ('Zona foto', 'Zona foto'),
        ('Fantana arteziana', 'Fantana arteziana'),
        ('Loc de joaca', 'Loc de joaca'),
        ('Gradina amenajata pentru cereemonie', 'Gradina amenajata pentru ceremonie'),
    )
    zona_exterioara_options = MultiSelectField(choices=zona_exterioara, default='')

    siguranta = (
        ('Alarma incendiu', 'Alarma incendiu'),
        ('Detectoare de fum', 'Detectoare de fum'),
        ('Acces ambulanta', 'Acces ambulanta'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Extinctoare', 'Extinctoare'),
        ('Serviciu de paza', 'Serviciu de paza'),
        ('Kit de prim ajutor', 'Kit de priim ajutor'),
    )
    siguranta_options = MultiSelectField(choices=siguranta, default='')



    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('saloon_details',kwargs={'id':self.pk})

    def get_update_url(self):
        return reverse('saloon_change',kwargs={'id':self.pk})






