from django.test import TestCase
from registration.forms import User

import finder
from finder.forms import UserForm, UserProfileForm, CommentForm
from finder.models import UserProfile, Comment
from django.forms import fields as django_fields


class TestForm(TestCase):

    def setUp(self):
        self.user_form = UserForm()
        self.user_profile_form = UserProfileForm()
        self.comment_form = CommentForm()

    def test_user_form_exist(self):
        self.assertTrue("UserForm" in dir(finder.forms))

    def test_user_form_link(self):
        self.assertEqual(type(self.user_form.__dict__['instance']), User)

    def test_user_form_fields(self):
        fields = self.user_form.fields
        expected_fields = {
            "password": django_fields.CharField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))

    def test_user_profile_form_exist(self):
        self.assertTrue("UserProfileForm" in dir(finder.forms))

    def test_user_profile_form_link(self):
        self.assertEqual(type(self.user_profile_form.__dict__['instance']), UserProfile)

    def test_comment_form_exist(self):
        self.assertTrue("CommentForm" in dir(finder.forms))

    def test_comment_form_link(self):
        self.assertEqual(type(self.comment_form.__dict__['instance']), Comment)

    def test_comment_form_fields(self):
        fields = self.comment_form.fields
        expected_fields = {
            "c_id": django_fields.CharField,
            "content": django_fields.CharField,
            "rate": django_fields.ChoiceField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))
