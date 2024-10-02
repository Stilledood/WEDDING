from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import BallRoom


class AllSaloons(View):
    '''Class to display all saloons '''

    template_name = 'all_saloons.html'
    model_name = BallRoom

    def get(self,request):
        all_saloons = self.model_name.objects.all()
        context={
            'all_salons':all_saloons
        }
        return render(request,template_name=self.template_name,context=context)


class AllSalonsByCounty(View):
    '''Class to display all saloons filtered by county'''

    template_name = 'Saloane/all_ballroms_county.html'
    model = BallRoom
    

    def get(self,request,county):
        ballrooms = self.model.objects.filter(county=county)
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







