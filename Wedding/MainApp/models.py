from django.db import models

class PlatformCLient(models.Model):
    '''Class to define a bastract structure for all platform clients'''

    client_name = models.CharField(max_length=250)
    client_email = models.EmailField()
    client_phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True

