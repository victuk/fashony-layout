from django import forms
from django.forms import ModelForm
class ContactForm(forms.Form):
    fullName = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))