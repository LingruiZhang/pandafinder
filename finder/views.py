from django.contrib.auth import authenticate, login
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.urls import reverse

from finder.models import Restaurant, Comment
from finder.forms import CommentForm, UserForm, UserProfileForm
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


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # 'registered': registered之后可能会删掉，现在不确定
    return render(request, 'finder/register.html', context={'user_form': user_form,
                                                            'profile_form': profile_form,
                                                            'registered': registered
                                                            })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('finder:index'))
            else:
                return HttpResponse("Your finder account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'finder/login.html')