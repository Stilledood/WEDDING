from django.db import models
from django.shortcuts import reverse,redirect
from multiselectfield import MultiSelectField
from ..MainApp.models import CLientDetails

class FotoVideo(CLientDetails):
    '''Class to construct a model for photographers and videographers'''

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
        ('Fotografie','Fotografie'),
        ('Video','Video'),
        ('Cabina Foto','Cabina Foto')
    )
    servicii_fotovideo = MultiSelectField(choices=servicii,default='')

    facilitati = (
        ('2 operatori','2 operatori'),
        ('Albume', 'Albume'),
        ('Drona', 'Drona'),
        ('Macara','Macara'),
        ('Slide','Slide'),
        ('Steady','Steady'),
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fotovideo_details',kwargs={'pk':self.pk})


