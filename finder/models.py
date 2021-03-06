from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneNumberField(unique=True, null=False, blank=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    r_id = models.CharField(max_length=20, primary_key=True, unique=True)
    r_name = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    r_phone_num = PhoneNumberField(unique=True, null=False, blank=False)
    r_email = models.CharField(max_length=30)
    website_url = models.URLField()
    menu = models.ImageField()
    photo = models.ImageField()
    overall_rate = models.FloatField(null=True)
    category = models.CharField(max_length=10)
    lat = models.FloatField(default=55.8642)
    lng = models.FloatField(default=-4.2518)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.r_id)
        super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.r_name


class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True, default=None)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, default=None)
    c_id = models.CharField(max_length=20, primary_key=True, unique=True)
    content = models.TextField(default="")
    rate = models.IntegerField(default=5)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.c_id
