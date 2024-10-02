from django.shortcuts import render, get_object_or_404
from .models import Cofetarie, Catering
from django.views import View



class AllBaker(View):
    '''Class to construct a view to display all bakers'''

    template_name = 'Catering/all_bakers.html'
    model_name = Cofetarie

    def get(self,request):
        all_bakers = self.model_name.objects.all()
        context = {
            'all_bakers':all_bakers
        }
        return render(request,template_name=self.template_name,context=context)


class AllBakersByCounty(View):
    '''Class to display all bakers filtered by county'''

    template_name = 'Catering/all_bakers.html'
    model_name = Cofetarie
    def get(self,request,county):
        all_bakers = self.model_name.objects.filter(county=county)
        context = {
            'all_bakers':all_bakers
        }
        return render(request,template_name=self.template_name,context=context)

class BakersDetails(View):
    '''Class to display all the details for a baker shop'''

    template_name = 'Catering/bakers_details.html'
    model_name = Cofetarie

    def get(self,request,pk):
        baker = get_object_or_404(self.model_name,pk=pk)
        context = {
            'baker':baker
        }
        return render(request,template_name=self.template_name,context=context)

class AllCatering(View):
    '''Class to construct a view to display all catering objects'''

    model_name = Catering
    template_name = 'Catering/all_catering.html'
    def get(self,request):
        all_catering = self.model_name.objects.all()
        context = {'catering_list' : all_catering}
        return render(request,self.template_name,context=context)

class AllCateringByCounty(View):
    '''Class to display all catering locations filtered by county'''

    template_name = 'Catering/all_catering_county.html'
    model_name = Catering

    def get(self,request,county):
        all_catering = self.model_name.objects.filter(county=county)
        context = {
            'all_catering':all_catering
        }
        return render(request,template_name=self.template_name,context=context)


class CateringDetails(View):
 '''Class to construct a view to display all details for a single catering object'''
 model_name = Catering
 template_name = 'Catering/catering_details.html'
 def get(self,request,pk):
     catering_object = get_object_or_404(self.model_name,pk=pk)
     context = {'catering':catering_object}
     return render(request,self.template_name,context=context)




