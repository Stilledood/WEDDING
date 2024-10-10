from .views import AllSaloons, SaloonDetails
from django.urls import re_path,path

urlpatterns = [
    path('',AllSaloons.as_view(),name='lista_saloane'),
    re_path(r'(?P<pk>\d+)/$',SaloonDetails.as_view(),name='saloon_details'),
]