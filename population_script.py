import os
import string
import random
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandafinder.settings')

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
            "content": "Good food, good services, pleasant staffs tell me that I should come back again to this place. You should come and try.",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c00003",
            "content": "Very delicious food and very excellent service.i'm so impressive.",
            "rate": 3,
            "user_id": "1234588",
        }

    ]

    restaurant2_comments = [

        {
            "c_id": "c00004",
            "content": "This is my first time here Great the experienced Food Delicious Friendly Staff very nice Will come again",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00005",
            "content": "Tasted very good",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c00006",
            "content": "Friendly service, good food. Dinner buffet was good all the way to desserts.",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant3_comments = [
        {
            "c_id": "c00007",
            "content": "It's our 3rd time here!!",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant4_comments = [
        {
            "c_id": "c00008",
            "content": "If you have the time try the dim sum , but if you don't have the time I suggest you don't eat there.Serving is very slow food is very slow too.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant5_comments = [
        {
            "c_id": "c00009",
            "content": "Seafood were pretty good. Fresh crab and the fried fish delicious. Restaurant setting and it's really popular, every min there are people coming in. 2 levels of seating.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant6_comments = [
        {
            "c_id": "c00010",
            "content": "I took my mom here for a 50% off buffet via eatigo app. Most of the food tasted good tho, but some of it tasted just so average or lower that my expectation hotel standard. Service was good",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant7_comments = [
        {
            "c_id": "c00210",
            "content": "Best buffet dimsum in town both price and quality. Chefs cook most of the food fresh so you have to wait longer in peak time but worth every second.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant8_comments = [
        {
            "c_id": "c00011",
            "content": "Good service Good place and Good food. We will visit this chinese cusine again in nearly. Price reasonable. Many promotion can discount",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant9_comments = [
        {
            "c_id": "c000012",
            "content": "Great service when have few customer",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant10_comments = [
        {
            "c_id": "c00013",
            "content": "Enjoyed it!",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant11_comments = [
        {
            "c_id": "c00014",
            "content": "Food was amazing!",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant12_comments = [
        {
            "c_id": "c00015",
            "content": "Worth the wait",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant13_comments = [
        {
            "c_id": "c000016",
            "content": "AVOID AVOID AVOID",
            "rate": 3,
            "user_id": "123456",
        },
    ]

    restaurant14_comments = [
        {
            "c_id": "c00018",
            "content": "Unaccommodating of people with disabilities",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant15_comments = [
        {
            "c_id": "c00020",
            "content": "Wonderful breakfast and friendly staff",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00021",
            "content": "Wonderful breakfast and friendly staff",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant16_comments = [
        {
            "c_id": "c00022",
            "content": "My husband daughter and I visited today for brunch food was fabulous locally sourced ",
            "rate": 5,
            "user_id": "123456",
        },
    ]
    restaurant17_comments = [
        {
            "c_id": "c00023",
            "content": "2 visits in 2 days",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00024",
            "content": "Great food + Excellent Service",
            "rate": 3,
            "user_id": "1234588",
        }
    ]
    restaurant18_comments = [
        {
            "c_id": "c00025",
            "content": "Huge space and beautiful. All the food that i had was really delicious and staff are really professional",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00026",
            "content": "Good taste good service. They have many choices of dimsum delicious everythings. You must try you will like it !!!",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant19_comments = [
        {
            "c_id": "c00027",
            "content": "Great food with a bargain!",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00028",
            "content": "Nice lunch with eat and trip group",
            "rate": 4,
            "user_id": "1234588",
        }
    ]

    restaurant20_comments = [
        {
            "c_id": "c00029",
            "content": "This restaurant offers good dim sum buffet with friendly price. The service also above standard. Recommended menu is roasted duck.",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00030",
            "content": "Everything is perfect.I never meet just like this before.I can’t explain by word.You should try this by youself.",
            "rate": 4,
            "user_id": "1234588",
        }
    ]

    restaurant21_comments = [
        {
            "c_id": "c00031",
            "content": "Extremely yummy dimsum. Everything was amazing ... truly extraordinary :) I will be back soon for sure",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00032",
            "content": "Fabulous a la carte buffet",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant22_comments = [
        {
            "c_id": "c00033",
            "content": "Good food delicious A lot of food are fresh sweet Desert so sweet The cost is not expensive The Serviceman are polite",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00034",
            "content": "I  have been to this restaurant before for dim sum at lunch. This is my second visited at this place. I love the atmosphere, foods and service. ",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant23_comments = [
        {
            "c_id": "c00035",
            "content": "I’m enjoy this meal, what a good taste. I like their dumpling the most, not too salt, not too sweet, a little juicy but yummy a lot.",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00036",
            "content": "Excellent quality Warm services.",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant24_comments = [
        {
            "c_id": "c00037",
            "content": "The food are nice and well designed. Raw materials are fresh. I recommend you to try the lava bun and eeg tart, its was delicious. The staff are nice.",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00038",
            "content": "Excellent taste and service!",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant25_comments = [
        {
            "c_id": "c00039",
            "content": "Best Dim Sum and service",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00040",
            "content": "Good - All delicious",
            "rate": 3,
            "user_id": "1234588",
        }
    ]

    restaurant26_comments = [

        {
            "c_id": "c00041",
            "content": "This place is a hidden gem! The food is delicious, the servers are so friendly ",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00042",
            "content": "Never disappoints - highly recommend!",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c0043",
            "content": "The food from here is absolutely gorgeous",
            "rate": 3,
            "user_id": "1234588",
        }

    ]

    restaurant27_comments = [

        {
            "c_id": "c00044",
            "content": "Very tasty and the staff were very kind!",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00045",
            "content": "Seen so many awesome reviews, and no1 could be disappointed, the food is awesome, would recommend to anyone.",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c00046",
            "content": "bad restaurantfadsfas",
            "rate": 3,
            "user_id": "1234588",
        }]

    restaurant28_comments = [
        {
            "c_id": "c00047",
            "content": "Busy throughout early lunch. Good choices variet",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant29_comments = [
        {
            "c_id": "c00048",
            "content": "Great food and even better customer service.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant30_comments = [
        {
            "c_id": "c00049",
            "content": "The people thar work there are amazing",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant31_comments = [
        {
            "c_id": "c00050",
            "content": "Great food and amazing people, definitely worth the visit ",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant32_comments = [
        {
            "c_id": "c00051",
            "content": "Amazing smells amazing taste and friendly staff what a great find,",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant33_comments = [
        {
            "c_id": "c00052",
            "content": "Delicious food, excellent service and friendly environment!",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant34_comments = [
        {
            "c_id": "c000053",
            "content": "Good food, good service and value for money ",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant35_comments = [
        {
            "c_id": "c00054",
            "content": "I have already recommended this to quite a few friends and have had the same response from them all, reiterating good food, value and service.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant36_comments = [
        {
            "c_id": "c00055",
            "content": "having had an OK meal here a few years ago ",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant37_comments = [
        {
            "c_id": "c00056",
            "content": "Had a lovely, fresh meal here last week.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant38_comments = [
        {
            "c_id": "c000057",
            "content": "We had the set menu which is amazing value. ",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant39_comments = [
        {
            "c_id": "c00058",
            "content": "Lovely restaurant, attentive staff, interesting menu , well presented food with fabulous flavours. The deserts are awesome! Will certainly visit again.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant40_comments = [
        {
            "c_id": "c00059",
            "content": "Lovely food here in this restaurant ",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant41_comments = [
        {
            "c_id": "c00060",
            "content": "Definitely recommended. Attentive friendly staff and superb food at a reasonable price. ",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant42_comments = [

        {
            "c_id": "c00061",
            "content": "The food is delicious and the service is welcoming and genuine.",
            "rate": 5,
            "user_id": "123456",
        },

        {
            "c_id": "c00062",
            "content": "We were greeted very warmly by all staff which really makes a big difference.",
            "rate": 4,
            "user_id": "1234577",
        },

        {
            "c_id": "c00063",
            "content": "Visited with family (6 of us) and from start to finish it was a pleasure to be there. ",
            "rate": 3,
            "user_id": "1234588",
        }]

    restaurant43_comments = [
        {
            "c_id": "c00064",
            "content": "If you are in Glasgow, you must go here!",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant44_comments = [
        {
            "c_id": "c00065",
            "content": "Every course was amazing. I’m vegetarians and gluten-intolerant and there was tons to choose from",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant45_comments = [
        {
            "c_id": "c00066",
            "content": "Loved the food, best indian food i ever had",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant46_comments = [
        {
            "c_id": "c00067",
            "content": "Went for lunch for the first time and i was impressed. T",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant47_comments = [
        {
            "c_id": "c00068",
            "content": "Had a lovely time having lunch with a pal.",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant48_comments = [
        {
            "c_id": "c00069",
            "content": " The cocktails were amazing and the food was delicious",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant49_comments = [
        {
            "c_id": "c000070",
            "content": "Highly recommended",
            "rate": 5,
            "user_id": "123456",
        },
    ]

    restaurant50_comments = [
        {
            "c_id": "c00071",
            "content": "Amazing menu, amazing food ",
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
            "menu": "restaurant_images/0001_menu.png",
            "photo": "restaurant_images/0001_photo.png",
            "overall_rate": 3.7,
            "category": "Korean",
            "lat": 55.871872,
            "lng": -4.298550,
        },

        "0002": {
            "r_name": "New Golden Bell",
            "postcode": "G3 8TQ",
            "address": "1204 Argyle St, Finnieston, Glasgow",
            "r_phone_num": "0141 334 8114",
            "r_email": "chineseseafood@gmail.com",
            "website_url": "newgoldenbellonline.co.uk",
            "menu": "restaurant_images/0002_menu.png",
            "photo": "restaurant_images/0002_photo.png",
            "overall_rate": 4.2,
            "category": "Chinese",
            "lat": 55.871262,
            "lng": -4.298691,
        },
        "0003": {
            "r_name": "Little Curry House",
            "postcode": "G11 5RG",
            "address": "41 Byres Rd, Glasgow",
            "r_phone_num": "01413391339",
            "r_email": "info@littlecurryhouse.co.uk",
            "website_url": "https://littlecurryhouse.co.uk/",
            "menu": "restaurant_images/0003_menu.png",
            "photo": "restaurant_images/0003_photo.png",
            "overall_rate": 4.1,
            "category": "Indian",
            "lat": 55.871262,
            "lng": -4.3008815,
        },

        "0004": {
            "r_name": "Dumpling Monkey",
            "postcode": "G11 6PR",
            "address": "121 Dumbarton Rd, Glasgow",
            "r_phone_num": "01415838300",
            "r_email": "",
            "website_url": "https://dumplingmonkey.com/",
            "menu": "restaurant_images/0004_menu.png",
            "photo": "restaurant_images/0004_photo.png",
            "overall_rate": 3.5,
            "category": "Chinese",
            "lat": 55.870138,
            "lng": -4.298757,
        },

        "0005": {
            "r_name": "esushi",
            "postcode": "G12 8TD",
            "address": "130-132 Byres Rd, Glasgow",
            "r_phone_num": "01413398970",
            "r_email": "info@esushiglasgow.co.uk",
            "website_url": "https://www.esushiglasgow.co.uk/",
            "menu": "restaurant_images/0005_menu.png",
            "photo": "restaurant_images/0005_photo.png",
            "overall_rate": 4.5,
            "category": "Japanese",
            "lat": 55.873649,
            "lng": -4.295253,
        },

        "0006": {
            "r_name": "Celino's Partick",
            "postcode": "G11 6AB",
            "address": "235 Dumbarton Rd, Partick, Glasgow",
            "r_phone_num": "01413410311",
            "r_email": "",
            "website_url": "https://www.celinos.hungrrr.co.uk/",
            "menu": "restaurant_images/0006_menu.png",
            "photo": "restaurant_images/0006_photo.png",
            "overall_rate": 4.5,
            "category": "Western",
            "lat": 55.870695,
            "lng": -4.302922,
        },

        "0007": {
            "r_name": "Banana Leaf",
            "postcode": "G11 5RD",
            "address": "5 & 9 Byres Rd, Partick, Glasgow",
            "r_phone_num": "01413348899",
            "r_email": "",
            "website_url": "https://www.bananaleafglasgow.com/",
            "menu": "restaurant_images/0007_menu.png",
            "photo": "restaurant_images/0007_photo.png",
            "overall_rate": 4.4,
            "category": "Asian",
            "lat": 55.870806,
            "lng": -4.299267,
        },

        "0008": {
            "r_name": "The Peach Garden",
            "postcode": "G2 3BW",
            "address": "24 Renfrew St, Glasgow",
            "r_phone_num": "07886428018",
            "r_email": "",
            "website_url": "https://www.facebook.com/The-Peach-Garden-Restaurant-Glasgow-%E6%A1%83%E8%8A%B1%E6%BA%90-809815642689730/?utm_source=yell&utm_medium=referral&utm_campaign=yell",
            "menu": "restaurant_images/0008_menu.png",
            "photo": "restaurant_images/0008_photo.png",
            "overall_rate": 4.4,
            "category": "Chinese",
            "lat": 55.865324,
            "lng": -4.255118,
        },

        "0009": {
            "r_name": "Bar Soba",
            "postcode": "G12 8TB",
            "address": "116-122 Byres Rd, Glasgow",
            "r_phone_num": "01413575482",
            "r_email": "mitchelllane@barsoba.co.uk",
            "website_url": "https://www.barsoba.co.uk/",
            "menu": "restaurant_images/0009_menu.png",
            "photo": "restaurant_images/0009_photo.png",
            "overall_rate": 4.1,
            "category": "Bar",
            "lat": 55.872934,
            "lng": -4.295998,
        },

        "0010": {
            "r_name": "Cafe Andaluz West End",
            "postcode": "G12 8AA",
            "address": "2 Cresswell Ln, Hillhead, Glasgow",
            "r_phone_num": "01413391111",
            "r_email": "",
            "website_url": "https://www.barsoba.co.uk/",
            "menu": "restaurant_images/0010_menu.png",
            "photo": "restaurant_images/0010_photo.png",
            "overall_rate": 4.5,
            "category": "Bar",
            "lat": 55.860884,
            "lng": -4.252432,
        },

        "0011": {
            "r_name": "TastEast",
            "postcode": "G11 5QE",
            "address": "11-15 Hyndland St, Partick, Glasgow",
            "r_phone_num": "01413342312",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0011_menu.png",
            "photo": "restaurant_images/0011_photo.png",
            "overall_rate": 4.3,
            "category": "Asian",
            "lat": 55.871211,
            "lng": -4.302773,
        },

        "0012": {
            "r_name": "Ramen Dayo",
            "postcode": "G12 8SJ",
            "address": "31 Ashton Ln, Hillhead, Glasgow",
            "r_phone_num": "01413740254",
            "r_email": "",
            "website_url": "https://ramendayo.com/",
            "menu": "restaurant_images/0012_menu.png",
            "photo": "restaurant_images/0012_photo.png",
            "overall_rate": 4.3,
            "category": "Japanese",
            "lat": 55.874651,
            "lng": -4.292974,
        },

        "0013": {
            "r_name": "Loon Fung Cantonese Restaurant",
            "postcode": "G2 3LG",
            "address": "Sauchiehall St, City Centre, Glasgow",
            "r_phone_num": "01413321240",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0013_menu.jpg",
            "photo": "restaurant_images/0013_photo.jpg",
            "overall_rate": 4.4,
            "category": "Chinese",
            "lat": 55.865970,
            "lng": -4.269130,
        },

        "0014": {
            "r_name": "Ubiquitous Chip",
            "postcode": "G12 8SJ",
            "address": "12 Ashton Ln, Hillhead, Glasgow",
            "r_phone_num": "01413345007",
            "r_email": "",
            "website_url": "https://ubiquitouschip.co.uk/",
            "menu": "restaurant_images/0014_menu.png",
            "photo": "restaurant_images/0014_photo.png",
            "overall_rate": 4.5,
            "category": "Western",
            "lat": 55.874803,
            "lng": -4.293043,
        },

        "0015": {
            "r_name": "Bantawala by Masala twist",
            "postcode": "G12 8SN",
            "address": "192-194 Byres Rd, Hillhead, Glasgow",
            "r_phone_num": "01413393777",
            "r_email": "",
            "website_url": "https://www.masalatwist.co.uk/",
            "menu": "restaurant_images/0015_menu.png",
            "photo": "restaurant_images/0015_photo.png",
            "overall_rate": 5.0,
            "category": "Indian",
            "lat": 55.874696,
            "lng": -4.294037,
        },

        "0016": {
            "r_name": "Bibimbap",
            "postcode": "G11 6PL",
            "address": "2 Partick Bridge St, Partick, Glasgow",
            "r_phone_num": "01413343030",
            "r_email": "",
            "website_url": "https://bibimbapwest.com/",
            "menu": "restaurant_images/0016_menu.png",
            "photo": "restaurant_images/0016_photo.png",
            "overall_rate": 4.9,
            "category": "Korean",
            "lat": 55.869820,
            "lng": -4.299800,
        },

        "0017": {
            "r_name": "Sichuan House",
            "postcode": "G2 3HW",
            "address": "345-349 Sauchiehall St, Glasgow",
            "r_phone_num": "01413331788",
            "r_email": "",
            "website_url": "https://www.alleatapp.com/menu-sichuan-house",
            "menu": "restaurant_images/0017_menu.png",
            "photo": "restaurant_images/0017_photo.png",
            "overall_rate": 4.4,
            "category": "Chinese",
            "lat": 55.865609,
            "lng": -4.266164,
        },

        "0018": {
            "r_name": "Ka Ka Lok Chinese Restaurant",
            "postcode": "G3 6JD",
            "address": "175 St George's Rd, Glasgow",
            "r_phone_num": "01413536528",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0018_menu.png",
            "photo": "restaurant_images/0018_photo.png",
            "overall_rate": 3.3,
            "category": "Chinese",
            "lat": 55.869760,
            "lng": -4.269350,
        },

        "0019": {
            "r_name": "20’s Mamak",
            "postcode": "G3 6QX",
            "address": "67 Cambridge St, Glasgow",
            "r_phone_num": "01413320300",
            "r_email": "",
            "website_url": "https://2restaurant_images/000s-mamak.business.site",
            "menu": "restaurant_images/0019_menu.png",
            "photo": "restaurant_images/0019_photo.png",
            "overall_rate": 4.9,
            "category": "Asia",
            "lat": 55.866362,
            "lng": -4.259998,
        },

        "0020": {
            "r_name": "Ox and Finch",
            "postcode": "G3 7TF",
            "address": "920 Sauchiehall St, Finnieston, Glasgow",
            "r_phone_num": "01413398627",
            "r_email": "",
            "website_url": "http://www.oxandfinch.com/",
            "menu": "restaurant_images/0020_menu.png",
            "photo": "restaurant_images/0020_photo.png",
            "overall_rate": 4.9,
            "category": "Western",
            "lat": 55.865541,
            "lng": -4.284933,
        },

        "0021": {
            "r_name": "Number 16 Restaurant",
            "postcode": "G11 5JY",
            "address": "16 Byres Rd, Partick, Bearsden, Glasgow",
            "r_phone_num": "01413392544",
            "r_email": "",
            "website_url": "http://number16.co.uk/",
            "menu": "restaurant_images/0021_menu.jpg",
            "photo": "restaurant_images/0021_photo.jpg",
            "overall_rate": 4.9,
            "category": "Modern",
            "lat": 55.870729,
            "lng": -4.298880,
        },

        "0022": {
            "r_name": "Ka Pao Glasgow",
            "postcode": "G12 8BE",
            "address": "26 Vinicombe St, Glasgow",
            "r_phone_num": "01414836990",
            "r_email": "",
            "website_url": "https://www.ka-pao.com/",
            "menu": "restaurant_images/0022_menu.png",
            "photo": "restaurant_images/0022_photo.png",
            "overall_rate": 4.9,
            "category": "Western",
            "lat": 55.877164,
            "lng": -4.290428,
        },

        "0023": {
            "r_name": "Buck's Bar",
            "postcode": "G2 2RU",
            "address": "111 W Regent St, Glasgow ",
            "r_phone_num": " 0141 648 4842",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0023_menu.png",
            "photo": "restaurant_images/0023_photo.png",
            "overall_rate": 4.9,
            "category": "Uk",
            "lat": 55.863270,
            "lng": -4.259670,
        },

        "0024": {
            "r_name": "Non Viet Restaurant",
            "postcode": "G2 3LX",
            "address": "536 Sauchiehall St, Glasgow",
            "r_phone_num": "01413322975",
            "r_email": "",
            "website_url": "https://nonviet.co.uk/",
            "menu": "restaurant_images/0024_menu.jpg",
            "photo": "restaurant_images/0024_photo.jpg",
            "overall_rate": 4.9,
            "category": "Vietnam",
            "lat": 55.866377,
            "lng": -4.270203,
        },

        "0025": {
            "r_name": "Viva Brazil",
            "postcode": "G2 7HX",
            "address": "87-91 Bothwell St, Glasgow",
            "r_phone_num": "01412040240",
            "r_email": "",
            "website_url": "https://vivabrazilrestaurants.com/glasgow/",
            "menu": "restaurant_images/0025_menu.png",
            "photo": "restaurant_images/0025_photo.png",
            "overall_rate": 4.9,
            "category": "Brazil",
            "lat": 55.861200,
            "lng": -4.262490,

        },

        "0026": {
            "r_name": "Smashburger",
            "postcode": "G2 3EW",
            "address": "165 Sauchiehall St, Glasgow ",
            "r_phone_num": "0141 332 4554",
            "r_email": "",
            "website_url": "https://smashburger.com",
            "menu": "restaurant_images/0026_menu.jpg",
            "photo": "restaurant_images/0026_photo.jpg",
            "overall_rate": 4.9,
            "category": "USA",
            "lat": 55.864596,
            "lng": -4.257996,


        },

        "0027": {
            "r_name": "Bistro fast food",
            "postcode": "G2 2AE",
            "address": "53 W Regent St, Glasgow",
            "r_phone_num": "0141 332 5302",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0027_menu.jpg",
            "photo": "restaurant_images/0027_photo.jpg",
            "overall_rate": 4.9,
            "category": "Western",
            "lat": 55.862920,
            "lng": -4.256800,


        },

        "0028": {
            "r_name": "Hong Kong Chinese Food Bar",
            "postcode": "G51 4RX",
            "address": "1131 Govan Rd, Glasgow",
            "r_phone_num": "0141 445 1683",
            "r_email": "",
            "website_url": "https://www.just-eat.co.uk/restaurants-hongkong-g51",
            "menu": "restaurant_images/0028_menu.png",
            "photo": "restaurant_images/0028_photo.png",
            "overall_rate": 4.9,
            "category": "Chinese",
            "lat": 55.864070,
            "lng": -4.329560,
        },

        "0029": {
            "r_name": "Nando's Glasgow - Sauchiehall Street",
            "postcode": "G2 3EZ",
            "address": "263 Sauchiehall St, Glasgow ",
            "r_phone_num": "0141 353 3682",
            "r_email": "",
            "website_url": "https://www.nandos.co.uk/restaurants/glasgow-sauchiehall-street",
            "menu": "restaurant_images/0029_menu.png",
            "photo": "restaurant_images/0029_photo.png",
            "overall_rate": 4.9,
            "category": "Western",
            "lat": 55.865171,
            "lng": -4.262634,
        },

        "0030": {
            "r_name": "Wagah’s",
            "postcode": "G1 4EE",
            "address": "58 Howard St, Glasgow ",
            "r_phone_num": "0141 328 0805",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0030_menu.png",
            "photo": "restaurant_images/0030_photo.png",
            "overall_rate": 4.9,
            "category": "Western",
            "lat": 55.856360,
            "lng": -4.254670,

        },

        "0031": {
            "r_name": "Tennents Byres Rd Glasgow",
            "postcode": "G12 8TN",
            "address": "191 Byres Rd, Glasgow",
            "r_phone_num": "0141 339 7203",
            "r_email": "",
            "website_url": "https://www.thetennentsbarglasgow.co.uk",
            "menu": "restaurant_images/0031_menu.png",
            "photo": "restaurant_images/0031_photo.png",
            "overall_rate": 4.9,
            "category": "Uk",
            "lat": 55.874394,
            "lng": -4.294951,
        },

        "0032": {
            "r_name": "satu satu: Malaysian Chinese cafe",
            "postcode": "G3 6JA",
            "address": "93-97 St George's Rd, Glasgow",
            "r_phone_num": "0141 237 4522",
            "r_email": "",
            "website_url": "http://www.satusatu.co.uk",
            "menu": "restaurant_images/0032_menu.png",
            "photo": "restaurant_images/0032_photo.png",
            "overall_rate": 4.9,
            "category": "Chinese",
            "lat": 55.868280,
            "lng": -4.271260,
        },

        "0033": {
            "r_name": "Lettuce Eat",
            "postcode": "G2 8LT",
            "address": "361 Argyle St, Glasgow ",
            "r_phone_num": "0141 221 3233",
            "r_email": "",
            "website_url": "https://bibimbapwest.com/",
            "menu": "restaurant_images/0033_menu.png",
            "photo": "restaurant_images/0033_photo.png",
            "overall_rate": 4.9,
            "category": "Western",
            "lat": 55.858832,
            "lng": -4.263266,

        },

        "0034": {
            "r_name": "Wolf Italian Street Food Glasgow",
            "postcode": "G2 7JZ",
            "address": "93-97 St George's Rd, Glasgow",
            "r_phone_num": "0141 237 4515",
            "r_email": "",
            "website_url": "https://bibimbapwest.com/",
            "menu": "restaurant_images/0034_menu.png",
            "photo": "restaurant_images/0034_photo.png",
            "overall_rate": 4.9,
            "category": "Italian",
            "lat": 55.861260,
            "lng": -4.262720,
        },

        "0035": {
            "r_name": "Two Fat Ladies at The Buttery",
            "postcode": "G3 8UF",
            "address": "652 Argyle St, Glasgow ",
            "r_phone_num": "0141 221 8188",
            "r_email": "",
            "website_url": "https://twofatladiesrestaurant.com/buttery",
            "menu": "restaurant_images/0035_menu.png",
            "photo": "restaurant_images/0035_photo.png",
            "overall_rate": 4.9,
            "category": "UK",
            "lat": 55.860700,
            "lng": -4.272260,

        },

        "0036": {
            "r_name": "Amber Regent",
            "postcode": "G2 2RA",
            "address": "50 W Regent St, Glasgow",
            "r_phone_num": "01413311655",
            "r_email": "",
            "website_url": "https://www.amberregent.com/",
            "menu": "restaurant_images/0036_menu.png",
            "photo": "restaurant_images/0036_photo.png",
            "overall_rate": 4.9,
            "category": "Chinese",
            "lat": 55.863220,
            "lng": -4.256390,
        },

        "0037": {
            "r_name": "Thairiffic Restaurant",
            "postcode": "G2 3HQ",
            "address": "303 Sauchiehall St, Glasgow",
            "r_phone_num": "01413323000",
            "r_email": "",
            "website_url": "https://www.thairifficrestaurant.com/",
            "menu": "restaurant_images/0037_menu.png",
            "photo": "restaurant_images/0037_photo.png",
            "overall_rate": 4.9,
            "category": "Thai",
            "lat": 55.865217,
            "lng": -4.260271,
        },

        "0038": {
            "r_name": "Glaschu Restaurant & Bar",
            "postcode": "G1 3AB",
            "address": "32 Royal Exchange Square, Glasgow",
            "r_phone_num": "01412482214",
            "r_email": "",
            "website_url": "http://glaschurestaurant.co.uk/",
            "menu": "restaurant_images/0038_menu.png",
            "photo": "restaurant_images/0038_photo.png",
            "overall_rate": 4.9,
            "category": "Scotland",
            "lat": 55.860533,
            "lng": -4.253481,

        },

        "0039": {
            "r_name": "Bavaria Brauhaus",
            "postcode": "G2 6NU",
            "address": "30 Bothwell St, Glasgow ",
            "r_phone_num": "0141 457 7100",
            "r_email": "",
            "website_url": "https://www.bavariabrauhaus.com",
            "menu": "restaurant_images/0039_menu.png",
            "photo": "restaurant_images/0039_photo.png",
            "overall_rate": 4.9,
            "category": "Beer House",
            "lat": 55.861360,
            "lng": -4.259850,
        },

        "0040": {
            "r_name": "Sholeh Persian Restaurant",
            "postcode": "G5 8EJ",
            "address": "146-148, Nelson St, Glasgow ",
            "r_phone_num": "0141 418 0796",
            "r_email": "",
            "website_url": "hhttps://www.sholehglasgow.com",
            "menu": "restaurant_images/0040_menu.png",
            "photo": "restaurant_images/0040_photo.png",
            "overall_rate": 4.9,
            "category": "Persian",
            "lat": 55.853470,
            "lng": -4.263860,
        },

        "0041": {
            "r_name": "iCafe Kelvingrove",
            "postcode": "G3 6ND",
            "address": "250-254 Woodlands Rd, Kelvingrove, Glasgow",
            "r_phone_num": "0141 353 6469",
            "r_email": "",
            "website_url": "http://www.icafe.uk.com/",
            "menu": "restaurant_images/0041_menu.png",
            "photo": "restaurant_images/0041_photo.png",
            "overall_rate": 4.9,
            "category": "Cafe",
            "lat": 55.871154,
            "lng": -4.276876,
        },

        "0042": {
            "r_name": "Koko House",
            "postcode": "G12 8AQ",
            "address": "175 Great George St, Hillhead, Glasgow",
            "r_phone_num": "0141 588 3007",
            "r_email": "",
            "website_url": "https://www.kokohouse.co.uk/",
            "menu": "restaurant_images/0042_menu.png",
            "photo": "restaurant_images/0042_photo.png",
            "overall_rate": 4.9,
            "category": "Cafe",
            "lat": 55.875447,
            "lng": -4.292560,
        },

        "0043": {
            "r_name": "Indian Gallery",
            "postcode": "G2 3JD",
            "address": "450 Sauchiehall Street, Glasgow",
            "r_phone_num": "0141 332 3355",
            "r_email": "",
            "website_url": "http://www.theindiangallery.co.uk/",
            "menu": "restaurant_images/0043_menu.png",
            "photo": "restaurant_images/0043_photo.png",
            "overall_rate": 4.9,
            "category": "Indian",
            "lat": 55.865823,
            "lng": -4.265014,
        },

        "0044": {
            "r_name": "Indian Times Restaurant",
            "postcode": "G21 4JY",
            "address": "361 Edgefauld Rd, Glasgow",
            "r_phone_num": "0141 558 9999",
            "r_email": "",
            "website_url": "https://indiatimesonline.co.uk/",
            "menu": "restaurant_images/0044_menu.png",
            "photo": "restaurant_images/0044_photo.png",
            "overall_rate": 4.9,
            "category": "Indian",
            "lat": 55.882170,
            "lng": -4.221690,
        },

        "0045": {
            "r_name": "Saint Luke's & The Winged Ox",
            "postcode": "G40 2JZ",
            "address": "17 Bain St, Glasgow",
            "r_phone_num": "01415528378",
            "r_email": "",
            "website_url": "http://www.stlukesglasgow.com/",
            "menu": "restaurant_images/0045_menu.png",
            "photo": "restaurant_images/0045_photo.png",
            "overall_rate": 4.9,
            "category": "BBq",
            "lat": 55.854665,
            "lng": -4.234647,
        },

        "0046": {
            "r_name": "Village Curry House",
            "postcode": "G5 8DZ",
            "address": "129 Nelson St, Glasgow ",
            "r_phone_num": "0141 429 4610",
            "r_email": "",
            "website_url": "",
            "menu": "restaurant_images/0046_menu.png",
            "photo": "restaurant_images/0046_photo.png",
            "overall_rate": 4.9,
            "category": "Pakistani",
            "lat": 55.852950,
            "lng": -4.262300,
        },

        "0047": {
            "r_name": "I. J. Mellis Cheesemonger",
            "postcode": "G12 8EW",
            "address": "492 Great Western Rd, Glasgow",
            "r_phone_num": "0141 339 8998",
            "r_email": "",
            "website_url": "https://mellischeese.net/",
            "menu": "restaurant_images/0047_menu.png",
            "photo": "restaurant_images/0047_photo.png",
            "overall_rate": 4.9,
            "category": "Cheese Shop",
            "lat": 55.875485,
            "lng": -4.281628,
        },

        "0048": {
            "r_name": "I Chai Restaurant",
            "postcode": "G13 1JP",
            "address": "1015 Crow Rd, Anniesland, Glasgow",
            "r_phone_num": "0141 959 3900",
            "r_email": "",
            "website_url": "https://ichaiglasgow.com/",
            "menu": "restaurant_images/0048_menu.png",
            "photo": "restaurant_images/0048_photo.png",
            "overall_rate": 4.9,
            "category": "Chinese",
            "lat": 55.893693,
            "lng": -4.321961,
        },

        "0049": {
            "r_name": "Ice-ilicious",
            "postcode": "G22 5ER",
            "address": "214 Saracen St, Possilpark, Glasgow ",
            "r_phone_num": "0141 237 4380",
            "r_email": "",
            "website_url": "http://www.ice-ilicious.com/",
            "menu": "restaurant_images/0049_menu.png",
            "photo": "restaurant_images/0049_photo.png",
            "overall_rate": 4.9,
            "category": "Dessert",
            "lat": 55.883326,
            "lng": -4.253999,
        },

        "0050": {
            "r_name": "Marble Global Buffet",
            "postcode": "G1 3DX",
            "address": "42 Queen St, Glasgow ",
            "r_phone_num": "01414831777",
            "r_email": "",
            "website_url": "https://www.marblebuffet.com/",
            "menu": "restaurant_images/0050_menu.jpg",
            "photo": "restaurant_images/0050_photo.jpeg",
            "overall_rate": 4.9,
            "category": "Buffet",
            "lat": 55.8587721,
            "lng": -4.2543877,
        },
    }

    commends_list = [restaurant1_comments, restaurant2_comments, restaurant3_comments, restaurant4_comments,
                     restaurant5_comments, restaurant6_comments, restaurant7_comments, restaurant8_comments,
                     restaurant9_comments, restaurant10_comments,
                     restaurant11_comments, restaurant12_comments, restaurant13_comments, restaurant14_comments,
                     restaurant15_comments, restaurant16_comments, restaurant17_comments, restaurant18_comments,
                     restaurant19_comments, restaurant20_comments,
                     restaurant21_comments, restaurant22_comments, restaurant23_comments, restaurant24_comments,
                     restaurant25_comments, restaurant26_comments, restaurant27_comments, restaurant28_comments,
                     restaurant29_comments, restaurant30_comments,
                     restaurant31_comments, restaurant32_comments, restaurant33_comments, restaurant34_comments,
                     restaurant35_comments, restaurant36_comments, restaurant37_comments, restaurant38_comments,
                     restaurant39_comments, restaurant40_comments,
                     restaurant41_comments, restaurant42_comments, restaurant43_comments, restaurant44_comments,
                     restaurant45_comments, restaurant46_comments, restaurant47_comments, restaurant48_comments,
                     restaurant49_comments, restaurant50_comments, ]

    users = {
        "lingrui":
            {
                "password": "123456",
                "user_profile": {
                    "phone_num": "+4487654321",
                    "picture": "profile_images/lingrui.jpg",
                }
            },
        "rana":
            {
                "password": "123456",
                "user_profile": {
                    "phone_num": "+4487654322",
                    "picture": "profile_images/rana.png",
                }
            },
        "oliver":
            {
                "password": "123456",
                "user_profile": {
                    "phone_num": "+4487654323",
                    "picture": "profile_images/oliver.jpg",
                }
            },
        "tong":
            {
                "password": "123456",
                "user_profile": {
                    "phone_num": "+4487654324",
                    "picture": "profile_images/tong.jpg",
                }
            },
    }

    '''add users'''
    for username, user in users.items():
        print(username)
        print(user)
        u = add_user(username, user["password"])
        add_user_profile(u, user["user_profile"]["phone_num"], user["user_profile"]["picture"])

    '''add restaurants'''
    for r_id, restaurant in restaurants.items():
        add_restaurant(r_id, restaurant["r_name"], restaurant["postcode"],
                       restaurant["address"], restaurant["r_phone_num"],
                       restaurant["r_email"], restaurant["website_url"],
                       restaurant["menu"], restaurant["photo"],
                       restaurant["overall_rate"], restaurant["category"],
                       restaurant["lat"], restaurant["lng"])
    '''add comments'''
    for i in range(len(commends_list)):
        restaurant = Restaurant.objects.all()[i]
        for comment in commends_list[i]:
            userIndex = random.randint(0, 3)
            userprofile = UserProfile.objects.all()[userIndex]
            add_comment(restaurant, userprofile, comment["c_id"], comment["content"], comment["rate"])


def add_user_profile(user, phone_num, picture):
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.phone_num = phone_num
    user_profile.picture = picture
    user_profile.save()
    return user_profile


def add_user(username, password):
    user = User.objects.create_user(username=username, password=password)
    # user.password = password;
    user.save()
    return user


def add_comment(restaurant, userprofile, c_id, content, rate):
    c = Comment.objects.get_or_create(restaurant=restaurant, c_id=c_id)[0]
    c.userprofile = userprofile
    c.content = content
    c.rate = rate
    c.save()
    return c


def add_restaurant(r_id, r_name, postcode, address, r_phone_num, r_email, website_url, menu, photo, overall_rate,
                   category, lat, lng):
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
    r.lat = lat
    r.lng = lng
    r.save()
    return r


if __name__ == '__main__':
    populate()
