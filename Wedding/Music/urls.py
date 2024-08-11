from django.urls import re_path,path
from .views import AllFormations,FormationDetails

urlpatterns = [
    path('',AllFormations.as_view(),name='all-bands'),
    re_path(r'(?P<pk>\d+)/$',FormationDetails.as_view(),name='band-details'),
]
