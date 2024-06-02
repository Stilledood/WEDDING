from django.db import models

from multiselectfield import MultiSelectField






class BallRoom(models.Model):
    '''Class to construct a model for all ballrooms'''
    client_name = models.CharField(max_length=250)
    client_email = models.EmailField()
    client_phone_number = models.CharField(max_length=10)
    events = (
        ('NUNTA','Nunta'),
        ('BOTEZ','Botez'),
        ('CORPORATE','Corporate'),
        ('ALTELE','Altele')
    )
    minimum_guests_number = models.ImageField()
    maximum_guests_number = models.IntegerField()
    type_of_events = models.CharField(choices=events)
    facillities = (
        ('Aer Conditionat', 'Aer Conditionat'),
        ('Sistem de sonorizare', 'Sistem de sonorizare'),
        ('Lumini arhitecturale', 'Lumini arhitecturale'),
        ('Iluminat profesional', 'Iluminat profesional'),
        ('Ring de dans', 'Ring de dans'),
        ('Scenă pentru formație/muzicieni', 'Scenă pentru formație/muzicieni'),
        ('Decoratiuni incluse', 'Decoratiuni incluse'),
        ('Baie Separata', 'Baie Separata'),
        ('Prezidiu', 'Prezidiu')
    )
    location_facilities = models.CharField(choices=facillities)
    catering = (
        ('Bucatarie proprie','Bucatarie proprie'),
        ('Servicii de catering incluse sau opționale', 'Servicii de catering incluse sau opționale'),
        ('Meniuri speciale', 'Meniuri speciale'),
        ('Degustare meniu', 'Degustare meniu'),
        ('Serviciul ospatarilor gratuit', 'Serviciul ospatarilor gratuit'),
        ('Candy Bar', 'Candy Bar'),
        ('Shot Bar', 'Shot Bar'),
        ('Fruit Bar', 'Fruit Bar'),
        ('Cocktail Bar', 'Cocktail Bar')
    )
    catering_options = models.CharField(choices=catering)
    parking = (
        ('Parcare gratuita', 'Parcare gratuita'),
        ('Parcare platita', 'Parcare platita')
    )
    parking_options = models.CharField(choices=parking)



