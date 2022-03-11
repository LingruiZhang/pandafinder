from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
    user_id = forms.CharField(widget=forms.HiddenInput)

