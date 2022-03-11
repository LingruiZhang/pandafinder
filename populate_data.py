import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandafinder.settings')

import django

django.setup()
from finder.models import Restaurant, Comment


def populate():
    restaurant1_comments = [

        {
            "c_id": "c00001",
            "content": "nice restaurant",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00002",
            "content": "good restaurant",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c00003",
            "content": "bad restaurant",
            "rate": 3,
            "user_id": "1234588",
        }

    ]

    restaurant2_comments = [

        {
            "c_id": "c00004",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00005",
            "content": "good restaurantfadfa",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c00006",
            "content": "bad restaurantfadsfas",
            "rate": 3,
            "user_id": "1234588",
        }

    ]

    restaurants = {
        "0000001": {
            "r_name": "Kimchi Cult",
            "postcode": "G11 5RQ",
            "address": "14 Chancellor St, Glasgow",
            "r_phone_num": "0141 258 8081",
            "r_email": "koreanFiredChicken@gmail.com",
            "website_url": "kimchicult.com",
            "menu": "0000001_menu.png",
            "photo": "0000001_photo.png",
            "overall_rate": 3.7,
            "category": "Korean",
            "comments": restaurant1_comments
        },

        "0000002": {
            "r_name": "New Golden Bell",
            "postcode": "G3 8TQ",
            "address": "1204 Argyle St, Finnieston, Glasgow",
            "r_phone_num": "0141 334 8114",
            "r_email": "chineseseafood@gmail.com",
            "website_url": "newgoldenbellonline.co.uk",
            "menu": "0000002_menu.png",
            "photo": "0000002_photo.png",
            "overall_rate": 4.2,
            "category": "Chinese",
            "comments": restaurant2_comments
        }
    }





    for r_id, restaurant_data in restaurants.items():
        r = add_restaurant(r_id, restaurant_data["r_name"], restaurant_data["postcode"],
                           restaurant_data["address"], restaurant_data["r_phone_num"],
                           restaurant_data["r_email"], restaurant_data["website_url"],
                           restaurant_data["menu"], restaurant_data["photo"],
                           restaurant_data["overall_rate"], restaurant_data["category"],
                           restaurant_data["comments"])
        for c in restaurant_data["comments"]:
            add_comment(r, c["c_id"], c["content"], c["rate"], c["user_id"])

    for r in Restaurant.objects.all():
        print(r.r_name)
        for c in Comment.objects.filter(restaurant=r):
            print(c.content)


def add_comment(restaurant, c_id, content, rate, user_id):
    c = Comment.objects.get_or_create(restaurant=restaurant, c_id=c_id)[0]
    c.content = content
    c.rate = rate
    c.user_id = user_id
    c.save()
    return c


def add_restaurant(r_id, r_name, postcode, address, r_phone_num, r_email, website_url, menu, photo, overall_rate,
                   category, comments):
    r = Restaurant.objects.get_or_create(r_id=r_id)[0]
    r.r_name = r_name
    r.postcode = postcode
    r.address = address
    r.r_phone_num = r_phone_num
    r.r_email = r_email
    r.website_url = website_url
    r.menu = menu
    r.photo = photo
    r.overall_rate = overall_rate
    r.category = category
    r.comments = comments
    r.save()
    return r

def import_json():
    with open("restaurant_info.json") as f:
        restaurant_dict = json.load(f)
    for restaurant in restaurant_dict[:20]:
        add_restaurant(restaurant["_id"],
                       restaurant["BusinessName"],
                       restaurant["PostCode"],
                       "",
                       )


if __name__ == '__main__':
    populate()
