from django.db import models
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

class CLientDetails(models.Model):
    '''Class to create a abstract model class from which all models will inherit'''

    client_name = models.CharField(max_length=200)
    client_phone = models.CharField(max_length=10)
    client_email = models.EmailField()
    client_webpage = models.URLField()
    client_facebook_page = models.URLField()
    client_instagram_page = models.URLField()
    client_tiktok_page = models.URLField()
    client_adress = models.CharField(max_length=250)
    client_county = models.CharField(choices=zip(romanian_cities.keys(), romanian_cities.keys()), default='Bucuresti')
    client_city = models.CharField(max_length=255, choices=city_choices, default='Bucuresti')
    client_description = models.TextField()