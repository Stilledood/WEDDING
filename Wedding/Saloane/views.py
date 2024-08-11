from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import BallRoom

class AllSalons(View):
    template_name = 'Saloane/all_ballroms/html'
    model = BallRoom

    def get(self,request):
        ballrooms = self.model.objects.all()
        context = {'ballrom_list':ballrooms}
        return render(request,self.template_name,context=context)

class SaloonDetails(View):
    '''Class to construct a view to display a saloon details'''

    model_name = BallRoom
    template_name = 'saloon_details.html'
    def get(self,request,pk):
        saloon = get_object_or_404(self.model_name,pk=pk)
        context = {'saloon':saloon}
        return render(request,self.template_name,context=context)


class AllFormations(View):
    '''Class to create a list of all type of formations'''

    template_name = 'formation_list.html'
    model_name = Formation

    def get(self,request):
        all_formations = self.model_name.objects.all()
        context = {'formations':all_formations}
        return render(request,self.template_name,context=context)

class FormationDetails(View):
    '''Class to create a view to display a formation details'''
    template_name = 'formation_details.html'
    model_name = Formation

    def get(self,request,pk):
        band = get_object_or_404(self.model_name,pk=pk)
        context = {'band':band}
        return render(request,self.template_name,context=context)


def index(request):
    return render(request, 'index.html')

