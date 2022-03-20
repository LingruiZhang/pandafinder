from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from finder.models import Restaurant, UserProfile


class TestView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.restaurant = Restaurant.objects.create(
            r_id="0099",
            r_name="Test Restaurant",
            postcode="G3 8RY",
            address="Test Street",
            r_phone_num="+441234123123",
            r_email="test@123.com",
            website_url="www.test.com",
            menu="test_menu.png",
            photo="test_photo.png",
            overall_rate=5,
            category="TestCategory",
            lat=55,
            lng=6,
        )
        self.user = User.objects.create_user(
            username="test",
            password="654321",
        )

        self.userprofile = UserProfile.objects.create(
            user=self.user,
            phone_num="+447586124088",
            picture="/profile_images/lingrui.jpg"
        )

    def test_index_GET(self):
        response = self.client.get(reverse("finder:index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "finder/index.html")

    def test_search_GET(self):
        response = self.client.get(reverse("finder:search"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed((response, "finder/searchPage.html"))

    def test_searchResult_GET(self):
        response = self.client.get(reverse("finder:searchResult"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed((response, "finder/searchResultPage.html"))

    def test_restaurant_GET(self):
        response = self.client.get(reverse("finder:show_restaurant", args=["0099"]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed((response, "finder/restaurantPage/test-slug.html"))

    def test_register_GET(self):
        response = self.client.get(reverse("finder:register"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed((response, "finder/register.html"))

    def test_log_out_GET(self):
        response = self.client.get(reverse("finder:logout"))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed((response, "finder/index.html"))

    def test_index_POST(self):
        response = self.client.post(reverse("finder:index"), {
            "username": self.user.username,
            "password": self.user.password,
        })
        self.assertEquals(response.status_code, 200)


    def test_register_POST(self):
        response = self.client.post(reverse("finder:register"), {
            "username": "test2",
            "password": "123456",
            "phone_num": "+441234123123",
            "picture": "/test.png",
        })
        self.assertEquals(response.status_code, 200)
