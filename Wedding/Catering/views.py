from django.shortcuts import render,get_object_or_404
from .models import Cofetarie,Catering
from django.views import View

class AllCatering(View):
    '''Class to construct a view to display all catering objects'''

    model_name = Catering
    template_name = 'Catering/all_catering.html'

    def get(self,request):
        all_catering = self.model_name.objects.all()
        context = {'catering_list' : all_catering}

        return request(request,self.template_name,context=context)


 class CateringDetails(View):
     '''Class to construct a view to display all details for a single catering object'''

     model_name = Catering
     template_name = 'catering_details.html'

     def get(self,request,pk):
         catering_object = get_object_or_404(self.model_name,pk=pk)
         context = {'catering':catering_object}
         return render(request,self.template_name,context=context)

