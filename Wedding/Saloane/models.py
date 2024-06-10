from django.db import models




romanian_cities = {"Bucuresti": ["Bucharest", "Voluntari", "Rosu", "Fundeni"], "Cluj": ["Cluj-Napoca", "Floresti", "Turda", "Dej", "Campia Turzii", "Gherla", "Apahida", "Baciu"], "Iasi": ["Iasi", "Pascani", "Valea Lupului", "Valea Adanca", "Lunca Cetatuii", "Harlau", "Targu Frumos", "Podu Iloaiei", "Tomesti"], "Constanta": ["Constanta", "Medgidia", "Navodari", "Mangalia", "Valu lui Traian", "Cumpana", "Ovidiu", "Murfatlar", "Harsova"], "Timis": ["Timisoara", "Lugoj", "Dumbravita", "Sannicolau Mare", "Jimbolia"], "Brasov": ["Brasov", "Sacele", "Fagaras", "Zarnesti", "Codlea", "Rasnov", "Sanpetru"], "Dolj": ["Craiova", "Bailesti", "Filiasi", "Calafat", "Dabuleni", "Poiana Mare"], "Galati": ["Galati", "Tecuci", "Matca", "Pechea", "Liesti"], "Bihor": ["Oradea", "Salonta", "Marghita", "Sacueni", "Beius", "Alesd", "Valea lui Mihai"], "Prahova": ["Ploiesti", "Campina", "Baicoi", "Breaza", "Mizil", "Valenii de Munte", "Comarnic", "Boldesti-Scaeni", "Urlati", "Sinaia"], "Braila": ["Braila", "Ianca"], "Arad": ["Arad", "Santana", "Pecica", "Lipova", "Ineu"], "Arges": ["Pitesti", "Mioveni", "Campulung", "Curtea de Arges", "Costesti", "Topoloveni"], "Bacau": ["Bacau", "Onesti", "Comanesti", "Moinesti", "Buhusi", "Darmanesti", "Targu Ocna"], "Sibiu": ["Sibiu", "Media", "Cisnadie", "Avrig"], "Mures": ["Targu-Mures", "Reghin", "Sighisoara", "Tarnaveni", "Ludus", "Sovata", "Sangeorgiu de Mures"], "Maramures": ["Baia Mare", "Sighetu Marmatiei", "Borsa", "Viseu de Sus", "Baia-Sprie", "Targu Lapus", "Moisei", "Poienile de sub Munte"], "Buzau": ["Buzau", "Ramnicu Sarat", "Nehoiu"], "Valcea": ["Ramnicu Valcea", "Dragasani"], "Satu Mare": ["Satu Mare", "Carei", "Negresti-Oas"], "Botosani": ["Botosani", "Dorohoi", "Darabani", "Flamanzi"], "Suceava": ["Suceava", "Radauti", "Falticeni", "Campulung Moldovenesc", "Vicovu de Sus", "Gura Humorului", "Vatra Dornei", "Marginea", "Dolhasca", "Salcea", "Cajvana", "Liteni"], "Caras-Severin": ["Resita", "Caransebes", "Bocsa", "Oravita", "Moldova Noua"], "Mehedinti": ["Drobeta-Turnu Severin", "Strehaia", "Orsova"], "Neamt": ["Piatra Neamt", "Roman", "Targu Neamt", "Sabaoani"], "Bistrita-Nasaud": ["Bistrita", "Beclean", "Sangeorz-Bai", "Nasaud"], "Gorj": ["Targu Jiu", "Motru", "Rovinari"], "Dambovita": ["Targoviste", "Moreni", "Pucioasa", "Gaesti", "Titu"], "Vrancea": ["Focsani", "Adjud", "Marasesti", "Odobesti"], "Tulcea": ["Tulcea", "Babadag"], "Alba": ["Alba Iulia", "Sebes", "Aiud", "Cugir", "Blaj", "Ocna Mures"], "Olt": ["Slatina", "Caracal", "Bals", "Corabia", "Scornicesti", "Draganesti-Olt"], "Vaslui": ["Vaslui", "Barlad", "Husi"], "Calarasi": ["Calarasi", "Oltenita"], "Giurgiu": ["Giurgiu", "Bolintin Vale"], "Ilfov": ["Popesti-Leordeni", "Bragadiru", "Pantelimon", "Otopeni", "Buftea", "Dudu", "Chitila", "Magurele", "Berceni", "Domnesti", "Jilava", "Mogosoaia", "Tunari", "Afumati"], "Hunedoara": ["Deva", "Hunedoara", "Petrosani", "Vulcan", "Petrila", "Lupeni", "Orastie", "Brad", "Simeria", "Calan", "Hateg"], "Salaj": ["Zalau", "Jibou"], "Covasna": ["Sfantu-Gheorghe", "Targu Secuiesc", "Covasna"], "Harghita": ["Miercurea-Ciuc", "Odorheiu Secuiesc", "Gheorgheni", "Toplita", "Cristuru Secuiesc"], "Ialomita": ["Slobozia", "Fetesti", "Cernavoda", "Urziceni"], "Teleorman": ["Alexandria", "Rosiori de Vede", "Turnu Magurele", "Zimnicea", "Videle"]}


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
    type_of_events = models.CharField(choices=events,default='')
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
        ('Numere pentru mese', 'Numere pentru mese'), \
        ('Loc de relaxare', 'Loc de relaxare '),
    )
    location_facilities = models.CharField(choices=facillities,default='')
    catering = (
        ('Bucatarie proprie','Bucatarie proprie'),
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
    catering_options = models.CharField(choices=catering,default='')
    parking = (
        ('Parcare gratuita', 'Parcare gratuita'),
        ('Parcare platita', 'Parcare platita'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Parcare iluminata', 'Parcare iluminata'),
    )
    parking_options = models.CharField(choices=parking,default='')
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
    zona_exterioara_options = models.CharField(choices=zona_exterioara,default='')

    siguranta = (
        ('Alarma incendiu', 'Alarma incendiu'),
        ('Detectoare de fum', 'Detectoare de fum'),
        ('Acces ambulanta', 'Acces ambulanta'),
        ('Supreaveghere video', 'Supraveghere video'),
        ('Extinctoare', 'Extinctoare'),
        ('Serviciu de paza', 'Serviciu de paza'),
        ('Kit de prim ajutor', 'Kit de priim ajutor'),
    )
    siguranta_options = models.CharField(choices=siguranta,default='')
    county = models.CharField(choices=zip(romanian_cities.keys(),romanian_cities.keys()),default='Bucuresti')
    city = models.CharField(choices=zip(romanian_cities[county],romanian_cities[county]),default='Bucuresti')
    adress = models.CharField(max_length=255,default='')