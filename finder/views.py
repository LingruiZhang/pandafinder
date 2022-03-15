from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.urls import reverse

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

def recalculate_overall_rate(restaurant_id_slug):
    restaurant = Restaurant.objects.get(slug=restaurant_id_slug)
    comments = Comment.objects.filter(restaurant=restaurant)
    total_rate = 0
    for comment in comments:
        total_rate += comment.rate
    overall_rate = total_rate/len(comments)
    restaurant.overall_rate = round(overall_rate, 1)
    restaurant.save()


def show_restaurant(request, restaurant_id_slug):
    context_dict = {}
    recalculate_overall_rate(restaurant_id_slug)
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_id_slug)
        comments = Comment.objects.filter(restaurant=restaurant)
        context_dict['restaurant'] = restaurant
        context_dict['comments'] = comments
    except Restaurant.DoesNotExist:
        context_dict['restaurant'] = None
        context_dict['comments'] = None

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        letters = string.ascii_letters
        if form.is_valid():
            comment = form.save(commit=False)
            comment.c_id = ''.join(random.choice(letters) for i in range(10))
            comment.restaurant = restaurant
            comment.user_id = "00001"
            comment.save()
            recalculate_overall_rate(restaurant_id_slug)
            return redirect(reverse('finder:show_restaurant', kwargs={'restaurant_id_slug':restaurant_id_slug}))
        else:
            print(form.errors)
    context_dict["form"] = form
    return render(request, "finder/restaurantPage.html", context=context_dict)


