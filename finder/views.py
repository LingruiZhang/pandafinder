from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse
from finder.models import Restaurant, Comment
from finder.forms import CommentForm, UserForm, UserProfileForm
import random
import string

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('finder:search'))
            else:
                return HttpResponse("Your finder account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'finder/index.html')


def search(request):
    restaurant_list = Restaurant.objects.order_by("overall_rate")
    context_dict = {"restaurants": restaurant_list}
    return render(request, "finder/searchPage.html", context=context_dict)


def searchResult(request):
    # restaurant_list = Restaurant.objects.order_by("overall_rate")
    if request.method == 'POST':
        query = request.POST.get('keyword')
        object_list = Restaurant.objects.filter(Q(r_name__icontains=query) | Q(address__icontains=query) | Q(category__icontains=query) | Q(postcode__icontains=query)).order_by('-overall_rate')[:10]
        return render(request, "finder/searchResultPage.html", context={'restaurants': object_list})
    else:
        return render(request, "finder/searchResultPage.html", context={'restaurants': None})


def recalculate_overall_rate(restaurant_id_slug):
    restaurant = Restaurant.objects.get(slug=restaurant_id_slug)
    comments = Comment.objects.filter(restaurant=restaurant)
    total_rate = 0
    for comment in comments:
        total_rate += comment.rate
    if len(comments) == 0:
        overall_rate = 0
    else:
        overall_rate = total_rate / len(comments)
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

        if request.user.is_authenticated:
            userprofile = request.user.userprofile
            if form.is_valid():
                comment = form.save(commit=False)
                comment.c_id = ''.join(random.choice(letters) for i in range(10))
                comment.restaurant = restaurant
                comment.userprofile = userprofile
                comment.save()
                recalculate_overall_rate(restaurant_id_slug)
                return redirect(reverse('finder:show_restaurant', kwargs={'restaurant_id_slug': restaurant_id_slug}))
            else:
                print(form.errors)
    context_dict["form"] = form
    context_dict["link"] = request.build_absolute_uri
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
    return render(request, 'finder/register.html', context={'user_form': user_form,
                                                            'profile_form': profile_form,
                                                            'registered': registered
                                                            })


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('finder:index'))