from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the templates engine.
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    # Render the response and send it back!
    return render(request, 'finder/index.html', context=context_dict)


def about(request):
    print(request.method)
    print(request.user)
    context_dict = {'boldmessage': 'Bing Dwen Dwen'}
    return render(request, 'finder/about.html', context=context_dict)