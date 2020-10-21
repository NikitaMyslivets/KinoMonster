from django import forms


class HelloForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, required=True)
    age = forms.IntegerField(min_value=0, max_value=110, required=True)