from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from ..Saloane.models import BallRoom



class SaloonList(View):
    '''Class to construct the view for list of all salons'''

    template_name = 'Saloane/saloon_list.html'
    model_name = BallRoom

    def get(self,request):
        saloon_list = self.model.objects.all()
        context = {'saloons':saloon_list}
        return render(request,self.template_name,context=context)


class SaloonDetails(View):
    '''Class to create a view to display a saloon details'''

    model_name = BallRoom
    template_name = 'Saloane/saloon_details.html'

    def get(self,request,pk):
        saloon = get_object_or_404(self.model_name,pk=pk)
        context = {'saloon':saloon}
        return render(request,self.template_name,context=context)





