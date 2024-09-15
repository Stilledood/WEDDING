from django.db import models
from django.shortcuts import  redirect,reverse
from multiselectfield import MultiSelectField
from ..MainApp.models import CLientDetails


class MakeUpSaloon(CLientDetails):
    '''Class to construct a model for makeup saloons'''

    servicies_makeup = (
        ('Accesorii Par','Accesorii Par'),
        ('Bronzare','Bronzare'),
        ('Extensii Par','Extensii Par')
    )

    servicies_field = MultiSelectField(choices=servicies_makeup,default='')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('makeup_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('makeup_update',kwargs={'pk':self.pk})

