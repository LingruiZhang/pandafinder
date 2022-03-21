from django.test import TestCase
from django.urls import reverse, resolve
from finder.views import search, register, searchResult, show_restaurant, user_logout, index


class TestUrl(TestCase):

    def setUp(self):
        pass

    def test_index_url(self):
        url = reverse("finder:index")
        self.assertEquals(resolve(url).func, index)

    def test_search_url(self):
        url = reverse("finder:search")
        self.assertEquals(resolve(url).func, search)

    def test_register_url(self):
        url = reverse("finder:register")
        self.assertEquals(resolve(url).func, register)

    def test_searchResult_url(self):
        url = reverse("finder:searchResult")
        self.assertEquals(resolve(url).func, searchResult)

    def test_restaurant_url(self):
        url = reverse("finder:show_restaurant", args=["test-slug"])
        self.assertEquals(resolve(url).func, show_restaurant)

    def test_logout_url(self):
        url = reverse("finder:logout")
        self.assertEquals(resolve(url).func, user_logout)
