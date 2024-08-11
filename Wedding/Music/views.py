from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Formation


class AllFormations(View):
    '''Class to create a list of all type of formations'''

    template_name = 'formation_list.html'
    model_name = Formation

    def get(self,request,county):
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