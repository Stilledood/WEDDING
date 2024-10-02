from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from models import FotoVideo


class AllFotoVideo(View):
    '''Class to create a view to display all FotoVideo clients'''

    template_name = 'FotoVideo/all_fotovideo.html'
    model_name = FotoVideo

    def get(self,request):
        all_fotovideo = self.model_name.objects.all()
        context = {
            'fotovideo':all_fotovideo
        }
        return render(request,template_name=self.template_name,context=context)


class AllFotoVideoByCounty(View):
    '''Class to display all fotovideo clients filtered by county'''

    template_name = 'FotoVideo/all_fotovideo.html'
    model_name = FotoVideo

    def get(self,request,county):
        fotovideo = self.model_name.objects.filter(county=county)
        context = {
            'fotovideo' : fotovideo
        }
        return render(request,template_name=self.template_name,context=context)


class FotoVideoDetails(View):
    '''Class to display details about one fotovideo client'''

    template_name = 'Catering/fotovideo_details.html'
    model_name = FotoVideo

    def get(self,request,pk):
        fotovideo = get_object_or_404(self.model_name,pk=pk)
        context = {
            'fotovideo':fotovideo
        }
        return render(request,template_name=self.template_name,context=context)
