from dataclasses import field
from socket import fromshare
from tokenize import Number
from django import forms



class size_form(forms.Form):
    saple_length=forms.FloatField()
    saple_width=forms.FloatField()
    patle_length=forms.FloatField()
    patle_width=forms.FloatField()

