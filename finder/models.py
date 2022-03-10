from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.template.defaultfilters import slugify


class Restaurant(models.Model):
    r_id = models.CharField(max_length=20, primary_key=True, unique=True)
    r_name = models.CharField(max_length=30)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneNumberField(unique = True, null = False, blank = False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
        
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    r_name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=6)
    address = models.CharField(max_length=200)
    r_phone_num =PhoneNumberField(unique = True, null = False, blank = False)
    r_email = models.EmailField(max_length=254)
    website_url = models.URLField()
    menu = models.ImageField()
    photo = models.ImageField()
    overall_rate = models.FloatField(null=True)
    category = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.r_id)
        super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.r_name

class Comment(models.Model):
    c_id = models.CharField(max_length=20, unique=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    content = models.TextField(default="")
    rate = models.FloatField(default=0)
    user_id = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.c_id

