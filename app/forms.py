from django import forms
from app.models import *

class prospects(forms.ModelForm):

    class Meta:
        model= prospects
        fields=('name', 'email','type','feel','description','budget',)

class feedbackform(forms.ModelForm):

    class Meta:
        model= feedback
        fields=('name', 'email', 'enquiry','question','number',)
