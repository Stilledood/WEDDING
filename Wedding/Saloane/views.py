from django.shortcuts import render
from django.views import View
from .models import BallRoom

class AllSalons(View):
    template_name = 'Saloane/all_ballroms/html'
    model = BallRoom

    def get(self,request):
        ballrooms = self.model.objects.all()
        context = {'ballrom_list':ballrooms}
        return render(request,self.template_name,context=context)


