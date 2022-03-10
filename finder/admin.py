from django.contrib import admin

# Register your models here.
from django.contrib import admin
from finder.models import Restaurant, Comment

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("r_id", )}





admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Comment)