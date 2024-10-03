from django.shortcuts import render, get_object_or_404
from .models import MakeUpSaloon
from django.views.generic import View


class AllMakeUpSaloons(View):
    '''Class to display all makeup saloons'''

    model_name = MakeUpSaloon
    template_name = 'HairMakeUp/all_makeup.html'

    def get(self,request):
        all_makeup = self.model_name.all()
        context = {
            'makeup' : all_makeup
        }
        return render(request,template_name=self.template_name,context=context)


class AllMakeUpSalonsByCounty(View):
    '''Class to construct a view to display all makeup saloons filtered by county'''

    template_name = 'HairMakeUp/all_makeup.html'
    model_name = MakeUpSaloon

    def get(self,request,county):
        makeup = self.model_name.objects.filter(county=county)
        context = {
            'makeup':makeup
        }
        return render(request,template_name=self.template_name,context=context)


class MakeUpSaloonDetails(View):
    '''Class to construct a view to display all details for a specific makeup saloon'''

    template_name = 'HairMaleUp/makeup_details.html'
    model_name = MakeUpSaloon

    def get(self,request,pk):
        makeup = get_object_or_404(self.model_name,pk=pk)
        context = {
            'makeup':makeup
        }
        return render(request,template_name=self.template_name,context=context)






