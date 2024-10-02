from django.shortcuts import render
from .models import MakeUpSaloon
from django.views.generic import View


class AllMakeUpSaloons(View):
    '''Class to display all makeup saloons'''

    model_name = MakeUpSaloon
    template_name = 'all_makeup.html'

    def get(self,request):

        all_makeup = self.model_name.all()


