__author__ = 'babayega'

from django import forms

class ContactUs(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
