from django.contrib.auth.models import User
from django.test import TestCase

from finder.models import UserProfile, Restaurant, Comment


class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="654321",
        )

        self.userprofile = UserProfile.objects.create(
            user=self.user,
            phone_num="+447586124088",
            picture="/profile_images/lingrui.jpg"
        )

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

        self.comment = Comment.objects.create(
            restaurant=self.restaurant,
            userprofile=self.userprofile,
            c_id="testCommentID",
            content="testContent",
            rate=5
        )

    def test_userprofile_model(self):
        self.assertEquals(self.userprofile.__str__(), self.userprofile.user.username)
        self.assertEquals(self.userprofile.phone_num, "+447586124088")
        self.assertEquals(self.user.username, "test")
        self.assertEquals(self.userprofile.picture, "/profile_images/lingrui.jpg")

    def test_restaurant_model(self):
        self.assertEquals(self.restaurant.__str__(), self.restaurant.r_name)
        self.assertEquals(self.restaurant.r_name, "Test Restaurant")
        self.assertEquals(self.restaurant.menu, "test_menu.png")
        self.assertEquals(self.restaurant.lat, 55)
        self.assertEquals(self.restaurant.slug, self.restaurant.r_id)

    def test_comment_model(self):
        self.assertEquals(self.comment.__str__(), self.comment.c_id)
        self.assertEquals(self.comment.content, "testContent")
        self.assertEquals(self.comment.rate, 5)

    def test_foreign_Key(self):
        self.assertEquals(self.comment.restaurant.r_id, self.restaurant.r_id)
        self.assertEquals(self.comment.userprofile.phone_num, self.userprofile.phone_num)
        self.assertEquals(self.userprofile.user.username, self.user.username)