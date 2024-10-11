from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from models import MagazinAccesorii, Jewelerry, Clothing

class AllClothing(View):
    '''Class to display all clothing clients'''

    model_name = Clothing
    template_name = 'all_clothing.html'

    def get(self,request):
        all_clothing = self.model_name.objects.all()
        context = {
            'all_clothing' : all_clothing
        }
        return render(request,template_name=self.template_name,context=context)



class AllClothingByCounty(View):
    '''Class to create a view to display all clothing clients filtered by county'''

    model_name = Clothing
    template_name = 'all_clothing.html'

    def get(self,request,county):
        all_clothing = self.model_name.objects.filter(county=county)
        context = {
            'all_clothing':all_clothing
        }
        return render(request,template_name=self.template_name,context=context)

class ClothingDetails(View):
    '''Class to create a view to display all details for a specific clothing client'''

    model_name = Clothing
    template_name = 'clothing_details.html'

    def get(self,request,pk):
        clothing = get_object_or_404(self.model_name,pk=pk)
        context = {
            'clothing':clothing
        }
        return render(request,template_name=self.template_name,context=context)

class AllJewels(View):
    '''class to construct a view to display all jewellery clients'''

    model_name = Jewelerry
    template_name = 'all_jewels.html'

    def get(self,request):
        all_jewels = self.model_name.objects.all()
        context = {
            'all_jewels':all_jewels
        }
        return render(request,template_name=self.template_name,context=context)

class AllJewelsByCounty(View):
    '''Class to construct a view to display all jewellery clients filtered by county'''

    model_name = Jewelerry
    template_name = 'all_jewels.html'

    def get(self,request,county):
        all_jewellery = self.model_name.objects.filter(county=county)
        context = {
            'all_jewellery':all_jewellery
        }
        return render(request,template_name=self.template_name,context=context)

class JewelleryDetails(View):
    '''Class to construct a view to display all details page for a jewellery client'''

    model_name = Jewelerry
    template_name = 'jewellery_details.html'

    def get(self,request,pk):
        jewel = get_object_or_404(self.model_name,pk=pk)
        context = {
            'jewel':jewel,
        }
        return render(request,template_name=self.template_name,context=context)

class AllAccesories(View):
    '''Class to construct a view to display all accesories clients'''

    model_name = MagazinAccesorii
    template_name = 'all_accesories.html'

    def get(self,request):
        accesories = self.model_name.objects.all()
        context = {
            'all_accesories':accesories
        }
        return render(request,template_name=self.template_name,context=context)


class AllAccesoriesByCounty(View):
    '''Class to construct a view to display all accesories clients filtered by county'''

    model_name = MagazinAccesorii
    template_name = 'all_accesories.html'

    def get(self,request,county):
        all_accesories = self.model_name.objects.filter(county=county)

        context = {
            'all_accesories': all_accesories
        }
        return render(request,template_name=self.template_name,context=context)


class AccesoriesDetails(View):
    '''Class to construct a view to display all details for a accesories client'''

    model_name = MagazinAccesorii
    template_name = 'accesories_details.html'

    def get(self,request,pk):
        accesories = get_object_or_404(self.model_name,pk=pk)
        context = {
            'accesories':accesories
        }
        return render(request,template_name=self.template_name,context=context)

