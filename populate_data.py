import json
import os
import string
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandafinder.settings')

import django

django.setup()
from finder.models import Restaurant, Comment, UserProfile
from django.contrib.auth.models import User

letters = string.ascii_letters


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
        }]

    restaurant3_comments = [
        {
            "c_id": "c00007",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant4_comments = [
        {
            "c_id": "c00008",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant5_comments = [
        {
            "c_id": "c00009",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant6_comments = [
        {
            "c_id": "c00010",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant7_comments = [
        {
            "c_id": "c00210",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant8_comments = [
        {
            "c_id": "c00011",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant9_comments = [
        {
            "c_id": "c000012",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant10_comments = [
        {
            "c_id": "c00013",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant11_comments = [
        {
            "c_id": "c00014",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant12_comments = [
        {
            "c_id": "c00015",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant13_comments = [
        {
            "c_id": "c000016",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant14_comments = [
        {
            "c_id": "c00018",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant15_comments = [
        {
            "c_id": "c00020",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant16_comments = [
        {
            "c_id": "c00022",
            "content": "nice restaurantfsadfaf",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurants = {
        "0001": {
            "r_name": "Kimchi Cult",
            "postcode": "G11 5RQ",
            "address": "14 Chancellor St, Glasgow",
            "r_phone_num": "0141 258 8081",
            "r_email": "koreanFiredChicken@gmail.com",
            "website_url": "kimchicult.com",
            "menu": "0001_menu.png",
            "photo": "0001_photo.png",
            "overall_rate": 3.7,
            "category": "Korean",
            "comments": restaurant1_comments
        },

        "0002": {
            "r_name": "New Golden Bell",
            "postcode": "G3 8TQ",
            "address": "1204 Argyle St, Finnieston, Glasgow",
            "r_phone_num": "0141 334 8114",
            "r_email": "chineseseafood@gmail.com",
            "website_url": "newgoldenbellonline.co.uk",
            "menu": "0002_menu.png",
            "photo": "0002_photo.png",
            "overall_rate": 4.2,
            "category": "Chinese",
            "comments": restaurant2_comments
        },
        "0003": {
            "r_name": "Little Curry House",
            "postcode": "G11 5RG",
            "address": "41 Byres Rd, Glasgow",
            "r_phone_num": "01413391339",
            "r_email": "info@littlecurryhouse.co.uk",
            "website_url": "https://littlecurryhouse.co.uk/",
            "menu": "0003_menu.png",
            "photo": "0003_photo.png",
            "overall_rate": 4.1,
            "category": "Indian",
            "comments": restaurant3_comments
        },

        "0004": {
            "r_name": "Dumpling Monkey",
            "postcode": "G11 6PR",
            "address": "121 Dumbarton Rd, Glasgow",
            "r_phone_num": "01415838300",
            "r_email": "",
            "website_url": "http://dumplingmonkey.com/",
            "menu": "0004_menu.png",
            "photo": "0004_photo.png",
            "overall_rate": 3.5,
            "category": "Chinese",
            "comments": restaurant4_comments
        },

        "0005": {
            "r_name": "esushi",
            "postcode": "G12 8TD",
            "address": "130-132 Byres Rd, Glasgow",
            "r_phone_num": "01413398970",
            "r_email": "info@esushiglasgow.co.uk",
            "website_url": "http://www.esushiglasgow.co.uk/",
            "menu": "0005_menu.png",
            "photo": "0005_photo.png",
            "overall_rate": 4.5,
            "category": "Japanese",
            "comments": restaurant5_comments
        },

        "0006": {
            "r_name": "Celino's Partick",
            "postcode": "G11 6AB",
            "address": "235 Dumbarton Rd, Partick, Glasgow",
            "r_phone_num": "01413410311",
            "r_email": "",
            "website_url": "https://www.celinos.hungrrr.co.uk/",
            "menu": "0006_menu.png",
            "photo": "0006_photo.png",
            "overall_rate": 4.5,
            "category": "Western",
            "comments": restaurant6_comments
        },

        "0007": {
            "r_name": "Banana Leaf",
            "postcode": "G11 5RD",
            "address": "5 & 9 Byres Rd, Partick, Glasgow",
            "r_phone_num": "01413348899",
            "r_email": "",
            "website_url": "https://www.bananaleafglasgow.com/",
            "menu": "0007_menu.png",
            "photo": "0007_photo.png",
            "overall_rate": 4.4,
            "category": "Asian",
            "comments": restaurant7_comments
        },

        "0008": {
            "r_name": "La Vita Spuntini",
            "postcode": "G12 8TN",
            "address": "199 Byres Rd, Glasgow",
            "r_phone_num": "01413394222",
            "r_email": "",
            "website_url": "https://la-vita-spuntini.co.uk/",
            "menu": "0008_menu.png",
            "photo": "0008_photo.png",
            "overall_rate": 4.4,
            "category": "Italian",
            "comments": restaurant8_comments
        },

        "0009": {
            "r_name": "Bar Soba",
            "postcode": "G12 8TB",
            "address": "116-122 Byres Rd, Glasgow",
            "r_phone_num": "01413575482",
            "r_email": "mitchelllane@barsoba.co.uk",
            "website_url": "https://www.barsoba.co.uk/",
            "menu": "0009_menu.png",
            "photo": "0009_photo.png",
            "overall_rate": 4.1,
            "category": "Bar",
            "comments": restaurant9_comments
        },

        "0010": {
            "r_name": "Cafe Andaluz West End",
            "postcode": "G12 8AA",
            "address": "2 Cresswell Ln, Hillhead, Glasgow",
            "r_phone_num": "01413391111",
            "r_email": "",
            "website_url": "https://www.barsoba.co.uk/",
            "menu": "0010_menu.png",
            "photo": "0010_photo.png",
            "overall_rate": 4.5,
            "category": "Bar",
            "comments": restaurant10_comments
        },

        "0011": {
            "r_name": "TastEast",
            "postcode": "G11 5QE",
            "address": "11-15 Hyndland St, Partick, Glasgow",
            "r_phone_num": "01413342312",
            "r_email": "",
            "website_url": "",
            "menu": "0011_menu.png",
            "photo": "0011_photo.png",
            "overall_rate": 4.3,
            "category": "Asian",
            "comments": restaurant11_comments
        },

        "0012": {
            "r_name": "Ramen Dayo",
            "postcode": "G12 8SJ",
            "address": "31 Ashton Ln, Hillhead, Glasgow",
            "r_phone_num": "01413740254",
            "r_email": "",
            "website_url": "https://ramendayo.com/",
            "menu": "0012_menu.png",
            "photo": "0012_photo.png",
            "overall_rate": 4.3,
            "category": "Japanese",
            "comments": restaurant12_comments
        },

        "0013": {
            "r_name": "Chaakoo West End",
            "postcode": "G12 9BG",
            "address": "61 Ruthven Ln, Glasgow",
            "r_phone_num": "01413348560",
            "r_email": "",
            "website_url": "https://www.chaakoo.co.uk/",
            "menu": "0013_menu.png",
            "photo": "0013_photo.png",
            "overall_rate": 4.4,
            "category": "Western",
            "comments": restaurant13_comments
        },

        "0014": {
            "r_name": "Ubiquitous Chip",
            "postcode": "G12 8SJ",
            "address": "12 Ashton Ln, Hillhead, Glasgow",
            "r_phone_num": "01413345007",
            "r_email": "",
            "website_url": "https://ubiquitouschip.co.uk/",
            "menu": "0014_menu.png",
            "photo": "0014_photo.png",
            "overall_rate": 4.5,
            "category": "Western",
            "comments": restaurant14_comments
        },

        "0015": {
            "r_name": "Bantawala by Masala twist",
            "postcode": "G12 8SN",
            "address": "192-194 Byres Rd, Hillhead, Glasgow",
            "r_phone_num": "01413393777",
            "r_email": "",
            "website_url": "http://www.masalatwist.co.uk/",
            "menu": "0015_menu.png",
            "photo": "0015_photo.png",
            "overall_rate": 5.0,
            "category": "Indian",
            "comments": restaurant15_comments
        },

        "0016": {
            "r_name": "Bibimbap",
            "postcode": "G11 6PL",
            "address": "2 Partick Bridge St, Partick, Glasgow",
            "r_phone_num": "01413343030",
            "r_email": "",
            "website_url": "https://bibimbapwest.com/",
            "menu": "0016_menu.png",
            "photo": "0016_photo.png",
            "overall_rate": 4.9,
            "category": "Korean",
            "comments": restaurant16_comments
        },
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

    users = {
        "test_user":
            {
                "password": "1234567",
                "user_profile": {
                    "phone_num": "+4487654321",
                    "picture": "profile_images/lingrui_profile.jpg",
                }
            }
    }

    for username, user in users.items():
        print(username)
        print(user)
        u = add_user(username, user["password"])
        add_user_profile(u, user["user_profile"]["phone_num"], user["user_profile"]["picture"])


def add_user_profile(user, phone_num, picture):
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.phone_num = phone_num
    user_profile.picture = picture
    user_profile.save()
    return user_profile


def add_user(username, password):
    user = User.objects.get_or_create(username=username)[0]
    user.password = password
    user.save()
    return user


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


if __name__ == '__main__':
    populate()
