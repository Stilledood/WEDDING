from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from ..Saloane.models import BallRoom
from ..Catering.models import Catering,Cofetarie
from ..FotoVideo.models import FotoVideo
from ..HairMakeUp.models import MakeUpSaloon
import random




class MainView(View):
    '''Class to construct a view for main page'''

    model_saloane = BallRoom
    model_catering = Catering
    model_cofetarie = Cofetarie
    model_foto_video = FotoVideo
    model_make_up = MakeUpSaloon
    template_name = 'index.html'

    def get(self,request):
        saloane = self.model_saloane.objects.all().order_by('?')[:10]
        catering = self.model_catering.objects.all().order_by('?')[:5]
        cofetarie = self.model_cofetarie.objects.all().order_by('?')[:5]
        foto_video = self.model_foto_video.objects.all().order_by('?')[:5]
        make_up = self.model_make_up.objects.all().order_by('?')[:5]

        context = {
            'saloane':saloane,
            'catering':catering,
            'cofetarii':cofetarie,
            'foto-video':foto_video,
            'make-up':make_up
        }

        return render(request,self.template_name,context=context)






