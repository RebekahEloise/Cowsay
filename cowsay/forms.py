from cowsay.models import Cowsay
from django import forms

class AddCowsayForm(forms.Form):
    cowsay_str = forms.CharField(max_length=100)
