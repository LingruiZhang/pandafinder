from django import forms
from django.contrib.auth.models import User
from django.db.models.functions import datetime

from finder.models import Comment, UserProfile


#oliver
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_num', 'picture',)



#lingrui
class CommentForm(forms.ModelForm):
    c_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    content = forms.CharField(widget=forms.Textarea, help_text="Please enter your comment!")
    rate = forms.IntegerField(help_text="Please rate by stars!")
    user_id = forms.CharField(widget=forms.HiddenInput, initial="0001")

    class Meta:
        model = Comment
        exclude = ('restaurant', "date")