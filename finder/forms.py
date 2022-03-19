from django import forms
from django.contrib.auth.models import User

from finder.models import Comment, UserProfile


# xunxi
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_num', 'picture',)


# lingrui
class CommentForm(forms.ModelForm):
    c_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    content = forms.CharField(widget=forms.Textarea, help_text="Please enter your comment!")
    rate_choices = [(i, i) for i in range(1, 6)]
    rate = forms.ChoiceField(widget=forms.RadioSelect(attrs={'index': 'value'}), choices=rate_choices, initial="5",
                             required=True, )

    class Meta:
        model = Comment
        exclude = ('restaurant', "userprofile", "date")
