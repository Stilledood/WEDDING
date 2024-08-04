from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def county_detail(request, county):
    context = {'county': county}
    return render(request, 'county_detail.html', context)
