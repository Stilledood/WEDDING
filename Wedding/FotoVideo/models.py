from django.db import models
from django.shortcuts import reverse,redirect
from multiselectfield import MultiSelectField
from MainApp.models import CLientDetails


class FotoVideo(CLientDetails):
    '''Class to construct a model for photographers and videographers'''


    servicii = (
        ('Fotografie','Fotografie'),
        ('Video','Video'),
        ('Cabina Foto','Cabina Foto'),
        ('Cabina 360', 'Cabina 360')
    )
    servicii_fotovideo = MultiSelectField(choices=servicii,default='')

    facilitati = (
        ('Multipli operatori','Multipli operatori'),
        ('Albume', 'Albume'),
        ('Drona', 'Drona'),
        ('Macara','Macara'),
        ('Slide','Slide'),
        ('Steady','Steady'),
    )
    facilities_selection = MultiSelectField(choices=facilitati, default='')

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('fotovideo_details',kwargs={'pk':self.pk})


