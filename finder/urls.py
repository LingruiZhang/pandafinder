from django.urls import path
from finder import views

app_name = 'finder'
urlpatterns = [
    path("", views.index, name='index'),
    path("search/", views.search, name='search'),
    path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    path("searchResult/", views.searchResult, name='searchResult'),
    path("restaurant/<slug:restaurant_id_slug>/", views.show_restaurant, name='show_restaurant'),
    path("logout/", views.user_logout, name='logout'),
]
