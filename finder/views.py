from django.shortcuts import render
from finder.models import Restaurant, Comment
from finder.forms import CommentForm
import random
import string
# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    
    return render(request, 'finder/index.html', context=context_dict)


def search(request):
    restaurant_list = Restaurant.objects.order_by("overall_rate")
    context_dict = {}
    context_dict["restaurants"] = restaurant_list

    return render(request, "finder/searchPage.html", context=context_dict)


def searchResult(request):
    restaurant_list = Restaurant.objects.order_by("overall_rate")
    context_dict = {}
    context_dict["restaurants"] = restaurant_list

    return render(request, "finder/searchResultPage.html", context=context_dict)




def show_restaurant(request, restaurant_id_slug):
    context_dict = {}
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_id_slug)
        comments = Comment.objects.filter(restaurant=restaurant)
        context_dict['restaurant'] = restaurant
        context_dict['comments'] = comments
    except Restaurant.DoesNotExist:
        context_dict['restaurant'] = None
        context_dict['comments'] = None
    return render(request, "finder/restaurantPage.html", context=context_dict)

