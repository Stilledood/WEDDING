from django.db import models
from MainApp.models import PlatformCLient
from multiselectfield import MultiSelectField

class BallRoom(PlatformCLient):
    '''Class to construct a model for all ballrooms'''
    events = (
        ('NUNTA','Nunta'),
        ('BOTEZ','Botez'),
        ('CORPORATE','Corporate'),
        ('ALTELE','Altele')
    )
    minimum_guests_number = models.ImageField()
    maximum_guests_number = models.IntegerField()
    type_of_events = MultiSelectField(choices=events)
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
    location_facilities = MultiSelectField(choices=facillities)
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
    catering_options = MultiSelectField(choices=catering)
    parking = (
        ('Parcare gratuita', 'Parcare gratuita'),
        ('Parcare platita', 'Parcare platita')
    )
    parking_options = MultiSelectField(choices=parking)
    main_image = models.ImageField(upload_to=f'media/{self.name}')


