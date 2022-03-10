from django import forms


class CommentForm(forms.ModelForm):
    c_id = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
    user_id = forms.CharField(widget=forms.HiddenInput)

