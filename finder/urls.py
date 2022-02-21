from django.urls import path
from finder import views
app_name = 'finder'
urlpatterns = [
    path('', views.index, name='index'),
]