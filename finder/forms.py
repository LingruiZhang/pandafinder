from django import forms
from django.db.models.functions import datetime

from finder.models import Comment


class CommentForm(forms.ModelForm):
    c_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    content = forms.CharField(widget=forms.Textarea, help_text="Please enter your comment!")
    rate = forms.FloatField(help_text="Please rate by stars!")
    user_id = forms.CharField(widget=forms.HiddenInput, initial="0001")

    class Meta:
        model = Comment
        exclude = ('restaurant', "date")