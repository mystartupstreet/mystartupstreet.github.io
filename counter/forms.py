__author__ = 'babayega'

from django import forms

class LetMeKnow(forms.Form):
    email = forms.EmailField()