from .views import SaloonDetails,AllSalons
from django.urls import re_path

urlpatterns = [
    re_path(r'(?P<pk>\d+)/$',SaloonDetails.as_view(),name='saloon_details'),
]