import os
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.deconstruct import deconstructible
from django.shortcuts import reverse,render,redirect

romanian_cities = {"Bucuresti": ["Bucharest", "Voluntari", "Rosu", "Fundeni"],
                   "Cluj": ["Cluj-Napoca", "Floresti", "Turda", "Dej", "Campia Turzii", "Gherla", "Apahida", "Baciu"],
                   "Iasi": ["Iasi", "Pascani", "Valea Lupului", "Valea Adanca", "Lunca Cetatuii", "Harlau",
                            "Targu Frumos", "Podu Iloaiei", "Tomesti"],
                   "Constanta": ["Constanta", "Medgidia", "Navodari", "Mangalia", "Valu lui Traian",
                                 "Cumpana", "Ovidiu", "Murfatlar", "Harsova"],
                   "Timis": ["Timisoara", "Lugoj", "Dumbravita", "Sannicolau Mare", "Jimbolia"],
                   "Brasov": ["Brasov", "Sacele", "Fagaras", "Zarnesti", "Codlea", "Rasnov", "Sanpetru"],
                   "Dolj": ["Craiova", "Bailesti", "Filiasi", "Calafat", "Dabuleni", "Poiana Mare"],
                   "Galati": ["Galati", "Tecuci", "Matca", "Pechea", "Liesti"],
                   "Bihor": ["Oradea", "Salonta", "Marghita", "Sacueni", "Beius", "Alesd", "Valea lui Mihai"],
                   "Prahova": ["Ploiesti", "Campina", "Baicoi", "Breaza", "Mizil", "Valenii de Munte", "Comarnic",
                               "Boldesti-Scaeni", "Urlati", "Sinaia"], "Braila": ["Braila", "Ianca"],
                   "Arad": ["Arad", "Santana", "Pecica", "Lipova", "Ineu"],
                   "Arges": ["Pitesti", "Mioveni", "Campulung", "Curtea de Arges", "Costesti", "Topoloveni"],
                   "Bacau": ["Bacau", "Onesti", "Comanesti", "Moinesti", "Buhusi", "Darmanesti", "Targu Ocna"],
                   "Sibiu": ["Sibiu", "Media", "Cisnadie", "Avrig"],
                   "Mures": ["Targu-Mures", "Reghin", "Sighisoara", "Tarnaveni", "Ludus", "Sovata",
                             "Sangeorgiu de Mures"],
                   "Maramures": ["Baia Mare", "Sighetu Marmatiei", "Borsa", "Viseu de Sus", "Baia-Sprie",
                                 "Targu Lapus", "Moisei", "Poienile de sub Munte"],
                   "Buzau": ["Buzau", "Ramnicu Sarat", "Nehoiu"],
                   "Valcea": ["Ramnicu Valcea", "Dragasani"],
                   "Satu Mare": ["Satu Mare", "Carei", "Negresti-Oas"],
                   "Botosani": ["Botosani", "Dorohoi", "Darabani", "Flamanzi"],
                   "Suceava": ["Suceava", "Radauti", "Falticeni", "Campulung Moldovenesc",
                               "Vicovu de Sus", "Gura Humorului", "Vatra Dornei", "Marginea", "Dolhasca",
                               "Salcea", "Cajvana", "Liteni"],
                   "Caras-Severin": ["Resita", "Caransebes", "Bocsa", "Oravita", "Moldova Noua"],
                   "Mehedinti": ["Drobeta-Turnu Severin", "Strehaia", "Orsova"],
                   "Neamt": ["Piatra Neamt", "Roman", "Targu Neamt", "Sabaoani"],
                   "Bistrita-Nasaud": ["Bistrita", "Beclean", "Sangeorz-Bai", "Nasaud"],
                   "Gorj": ["Targu Jiu", "Motru", "Rovinari"],
                   "Dambovita": ["Targoviste", "Moreni", "Pucioasa", "Gaesti", "Titu"],
                   "Vrancea": ["Focsani", "Adjud", "Marasesti", "Odobesti"],
                   "Tulcea": ["Tulcea", "Babadag"],
                   "Alba": ["Alba Iulia", "Sebes", "Aiud", "Cugir", "Blaj", "Ocna Mures"],
                   "Olt": ["Slatina", "Caracal", "Bals", "Corabia", "Scornicesti", "Draganesti-Olt"],
                   "Vaslui": ["Vaslui", "Barlad", "Husi"], "Calarasi": ["Calarasi", "Oltenita"],
                   "Giurgiu": ["Giurgiu", "Bolintin Vale"],
                   "Ilfov": ["Popesti-Leordeni", "Bragadiru", "Pantelimon", "Otopeni", "Buftea", "Dudu",
                             "Chitila", "Magurele", "Berceni", "Domnesti", "Jilava", "Mogosoaia", "Tunari", "Afumati"],
                   "Hunedoara": ["Deva", "Hunedoara", "Petrosani", "Vulcan", "Petrila", "Lupeni", "Orastie",
                                 "Brad", "Simeria", "Calan", "Hateg"], "Salaj": ["Zalau", "Jibou"],
                   "Covasna": ["Sfantu-Gheorghe", "Targu Secuiesc", "Covasna"],
                   "Harghita": ["Miercurea-Ciuc", "Odorheiu Secuiesc", "Gheorgheni", "Toplita", "Cristuru Secuiesc"],
                   "Ialomita": ["Slobozia", "Fetesti", "Cernavoda", "Urziceni"],
                   "Teleorman": ["Alexandria", "Rosiori de Vede", "Turnu Magurele", "Zimnicea", "Videle"]}
county = romanian_cities.keys()

if isinstance(county, str) and county in romanian_cities:
    city_choices = romanian_cities[county]
else:
    city_choices = ['Bucuresti']

city_choices = list(zip(city_choices, city_choices))


class BallRoom(models.Model):
    """Class to construct a model for all ballrooms"""
    client_name = models.CharField(max_length=250)
    client_email = models.EmailField()
    client_phone_number = models.CharField(max_length=10)
    events = (
        ('NUNTA', 'Nunta'),
        ('BOTEZ', 'Botez'),
        ('CORPORATE', 'Corporate'),
        ('ALTELE', 'Altele')
    )
    minimum_guests_number = models.IntegerField()
    maximum_guests_number = models.IntegerField()
    type_of_events = models.CharField(choices=events, default='')
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
    location_facilities = models.CharField(choices=facillities, default='')
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
    catering_options = models.CharField(choices=catering, default='')
    parking = (
        ('Parcare gratuita', 'Parcare gratuita'),
        ('Parcare platita', 'Parcare platita'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Parcare iluminata', 'Parcare iluminata'),
    )
    parking_options = models.CharField(choices=parking, default='')
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
    zona_exterioara_options = models.CharField(choices=zona_exterioara, default='')

    siguranta = (
        ('Alarma incendiu', 'Alarma incendiu'),
        ('Detectoare de fum', 'Detectoare de fum'),
        ('Acces ambulanta', 'Acces ambulanta'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Extinctoare', 'Extinctoare'),
        ('Serviciu de paza', 'Serviciu de paza'),
        ('Kit de prim ajutor', 'Kit de priim ajutor'),
    )
    siguranta_options = models.CharField(choices=siguranta, default='')
    county = models.CharField(choices=zip(romanian_cities.keys(), romanian_cities.keys()), default='Bucuresti')
    city = models.CharField(max_length=255, choices=city_choices, default='Bucuresti')
    adress = models.CharField(max_length=255, default='')
    descriere = models.TextField(default='Descriere')


    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('saloon_details',kwargs={'id':self.pk})

    def get_update_url(self):
        return reverse('saloon_change',kwargs={'id':self.pk})




class Anunt(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    type_event = (
        ('Salon', 'Salon'),
        ('Coafor', 'Coafor'),
        ('Catering', 'Catering'),
        ('Fotograf', 'Fotograf'),
        ('Valet', 'Valet')
    )

    type = models.CharField(max_length=255, choices=type_event, default='')
    county = models.CharField(choices=zip(romanian_cities.keys(), romanian_cities.keys()), default='Bucuresti')
    city = models.CharField(max_length=255, choices=city_choices, default='Bucuresti')
    adress = models.CharField(max_length=255, default='')
    phone = PhoneNumberField()
    contact_email = models.EmailField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'anunt'

    def __str__(self):
        return self.name


@deconstructible
class UploadToDirectory:
    def __call__(self, instance, filename):
        # Construct the directory path based on id_anunt
        dir_name = f"anunt_images/{instance.id_anunt}/"
        # Create the directory if it doesn't exist
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        return os.path.join(dir_name, filename)


class AttributeSalon(models.Model):
    id = models.AutoField(primary_key=True)
    id_anunt = models.IntegerField()
    min_guests = models.IntegerField()
    max_guests = models.IntegerField()
    type_events = models.TextField(blank=True)
    facilities = models.TextField(blank=True)
    catering = models.TextField(blank=True)
    zona_exterior = models.TextField(blank=True)
    parking = models.TextField(blank=True)
    saftey = models.TextField(blank=True)
    descriere = models.TextField(blank=True)
    image = models.FileField(upload_to=UploadToDirectory(), blank=True)

    class Meta:
        db_table = 'attribute_salon'

    def __str__(self):
        return self.descriere




class AttributeCoafor(models.Model):
    id = models.AutoField(primary_key=True)
    id_anunt = models.IntegerField()
    descriere = models.TextField(blank=True)
    type = models.CharField(max_length=255, default='')
    image = models.FileField(upload_to=UploadToDirectory(), blank=True)

    class Meta:
        db_table = 'attribute_coafor'

    def __str__(self):
        return self.descriere


class AttributeCatering(models.Model):
    id = models.AutoField(primary_key=True)
    id_anunt = models.IntegerField()
    descriere = models.TextField(blank=True)

    type_catering = (
        ('Corporate', 'Corporate'),
        ('Private', 'Private'),
        ('Nunta', 'Nunta'),
        ('Botez', 'Botez'),
    )

    type = models.CharField(max_length=255, choices=type_catering, default='')
    image = models.FileField(upload_to=UploadToDirectory(), blank=True)

    class Meta:
        db_table = 'attribute_catering'

    def __str__(self):
        return self.descriere


class AttributeFotograf(models.Model):
    id = models.AutoField(primary_key=True)
    id_anunt = models.IntegerField()
    descriere = models.TextField(blank=True)
    image = models.FileField(upload_to=UploadToDirectory(), blank=True)

    class Meta:
        db_table = 'attribute_fotograf'

    def __str__(self):
        return self.descriere


class AttributeValet(models.Model):
    id = models.AutoField(primary_key=True)
    id_anunt = models.IntegerField()
    descriere = models.TextField(blank=True)

    class Meta:
        db_table = 'attribute_valet'

    def __str__(self):
        return self.descriere
