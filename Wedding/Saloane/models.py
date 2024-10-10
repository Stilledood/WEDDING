
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse,render,redirect
from multiselectfield import MultiSelectField
from MainApp.models import CLientDetails







class BallRoom(CLientDetails):
    """Class to construct a model for all ballrooms"""

    maximum_guests_number = models.IntegerField()

    facillities = (
        ('Aer Conditionat', 'Aer Conditionat'),
        ('Sistem de sonorizare', 'Sistem de sonorizare'),
        ('Lumini arhitecturale', 'Lumini arhitecturale'),
        ('Iluminat profesional', 'Iluminat profesional'),
        ('Ring de dans', 'Ring de dans'),
        ('Scenă pentru formație/muzicieni', 'Scenă pentru formație/muzicieni'),
        ('Baie Separata', 'Baie Separata'),
        ('Prezidiu', 'Prezidiu'),
        ('Wifi', 'Wifi'),
        ('Proximitea centrului orasului', 'Proximitatea centrului orasului'),
        ('Foto corner', 'Foto corner'),
        ('Loc de relaxare', 'Loc de relaxare '),
        ('Grup sanitar persoane cu dizabilitati', 'Grup sanitar persoane cu dizabilitati'),

    )
    event_facilities = (
        ('Decoratiuni incluse', 'Decoratiuni incluse'),
        ('Decor mese', 'Decor mese'),
        ('Decor scaune', 'Decor scaune'),
        ('Meniuri pentru mese', 'Meniuri pentru mese'),
        ('Casuta de dar', 'Casuta de dar'),
        ('Event planner', 'Event planner'),
        ('Stativ cu lista invitatilor', 'Stativ cu lista invitatilor'),
        ('Numere pentru mese', 'Numere pentru mese'),
        ('Obiceiuri', 'Obiceiuri'),
        ('Masina de fum', 'Masina de fum'),
        ('Gheata Carbonica', 'Gheata Carbonica'),
        ('Efecte pirotehnice', 'Efecte pirotehnice')
    )
    event_facilities_selection = MultiSelectField(choices=event_facilities, default='')
    location_facilities = MultiSelectField(choices=facillities, default='')
    catering = (
        ('Meniu Personalizat', 'Meniu Personalizat'),
        ('Bucatarie proprie', 'Bucatarie proprie'),
        ('Servicii de catering incluse sau opționale', 'Servicii de catering incluse sau opționale'),
        ('Meniuri speciale', 'Meniuri speciale'),
        ('Degustare meniu', 'Degustare meniu'),
        ('Serviciul ospatarilor gratuit', 'Serviciul ospatarilor gratuit'),
        ('Candy Bar', 'Candy Bar'),
        ('Shot Bar', 'Shot Bar'),
        ('Fruit Bar', 'Fruit Bar'),
        ('Cocktail Bar', 'Cocktail Bar'),
        ('Open bar', 'Open bar'),
        ('All inclusive', 'All inclusive'),
        ('Cofetarie/Patiserie', 'Cofetarie/Patiserie'),

    )
    catering_options = MultiSelectField(choices=catering, default='')
    parking = (
        ('Parcare gratuita', 'Parcare gratuita'),
        ('Parcare privata', 'Parcare privata'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Parcare iluminata', 'Parcare iluminata'),
        ('Parcare interioara', 'Parcare interioara'),
        ('Drum asfaltat', 'Drum asfaltat'),
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
        ('Gradina amenajata pentru ceremonie', 'Gradina amenajata pentru ceremonie'),
        ('Locatie pe lac', 'Locatie pe lac'),
        ('Vedere la lac', 'Vedere la lac'),
        ('Locatie in padure', 'Locatie in padure'),
        ('Vedere panoramica', 'Vedere panoramica'),
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

    minim_menu_price = models.IntegerField(blank=True)
    meniu = models.FileField(upload_to='pdf-menus')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('saloon_details',kwargs={'id':self.pk})

    def get_update_url(self):
        return reverse('saloon_change',kwargs={'id':self.pk})






