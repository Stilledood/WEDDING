from django.shortcuts import render,get_object_or_404
from django.views import View
from models import Music


class AllFormations(View):
    '''Class to create a list of all type of formations'''

    template_name = 'Music/formation_list.html'
    model_name = Music

    def get(self,request,county):
        all_formations = self.model_name.objects.all()
        context = {'formations':all_formations}
        return render(request,self.template_name,context=context)


class AllFormationsByCounty(View):
    '''Class to construct a view to display all formations objects filtered by county'''

    template_name = 'Music/formation_list.html'
    model_name = Music

    def get(self,request,county):
        music = self.model_name.objects.filter(county=county)
        context = {
            'music':music
        }
        return render(request,template_name=self.template_name,context=context)

class FormationDetails(View):
    '''Class to create a view to display a formation details'''
    template_name = 'Music/formation_details.html'
    model_name = Music
    def get(self,request,pk):
        band = get_object_or_404(self.model_name,pk=pk)
        context = {'band':band}
        return render(request,self.template_name,context=context)