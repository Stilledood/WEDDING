from django.db import models
from django.shortcuts import  redirect,reverse
from multiselectfield import MultiSelectField
from ..MainApp.models import CLientDetails


class MakeUpSaloon(CLientDetails):
    '''Class to construct a model for makeup saloons'''

    name = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    meniu = models.FileField(upload_to='pdf-menus')
    instagram_page = models.URLField()
    tik_tok_page = models.URLField()
    facebook_page = models.URLField()
    website_page = models.URLField()

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

