from django.db import models
from django.shortcuts import reverse
from multiselectfield import MultiSelectField
from MainApp.models import CLientDetails


class Music(CLientDetails):
    '''Class to create a model for all music part'''


    formation_type = (
        ('Formatie', 'Formatie'), ('DJ', 'DJ')
    )

    musical_styles = (
        ('Clasic', 'Clasic'),
        ('Disco', 'Disco'),
        ('Folclor', 'Folclor'),
        ('Hip-Hop', 'Hip=Hop'),
        ('Instrumental', 'Instrumental'),
        ('Jazz', 'Jazz'),
        ('Latino', 'Latino'),
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Manele', 'Manele'),
        ('Lautareasca', 'Lautareasca'),
        ('Retro', 'Retro'),
        ('Mix','Mix'),
        ('Live', 'Live')
    )

    muscial_styles_field = MultiSelectField(choices=musical_styles, default='')
    tip = models.CharField(choices=formation_type, default='')



    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('detalii_muzica', kwargs={'id':self.pk})

    def get_update_url(self):
        return reverse('update_muzica', kwargs={'id':self.pk})
