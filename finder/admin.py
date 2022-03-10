from django.contrib import admin

# Register your models here.
from django.contrib import admin
from finder.models import Restaurant, Comment, UserProfile

admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(UserProfile)