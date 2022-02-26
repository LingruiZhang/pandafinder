from django.db import models


# Create your models here.






class Restaurant(models.Model):
    r_id = models.CharField(max_length=20, unique=True)
    r_name = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    r_phone_num = models.CharField(max_length=10)
    r_email = models.CharField(max_length=30)
    website_url = models.URLField()
    menu = models.ImageField()
    photo = models.ImageField()
    overall_rate = models.FloatField()
    category = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.r_name


class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    c_id = models.CharField(max_length=20, unique=True)
    content = models.TextField(default="")
    rate = models.FloatField(default=0)
    user_id = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.c_id
