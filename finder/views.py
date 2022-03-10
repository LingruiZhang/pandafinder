from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    
    return render(request, 'finder/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'Bing Dwen Dwen'}
    return render(request, 'finder/about.html', context=context_dict)