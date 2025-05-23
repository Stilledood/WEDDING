"""
URL configuration for Wedding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views
from Saloane import urls as saloane_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('indexold.html', TemplateView.as_view(template_name='indexold.html'), name='index'),
    path('properties.html', TemplateView.as_view(template_name='properties.html'), name='properties'),
    path('saloon_details.html', TemplateView.as_view(template_name='saloon_details.html'), name='property-details'),
    path('contact.html', TemplateView.as_view(template_name='contact.html'), name='contact'),
    re_path(r'^county/(?P<county>[a-zA-Z0-9_-]+)/$', views.county_detail, name='county_detail'),
    re_path(r'^saloane/',include(saloane_urls))
]
