from logging import PlaceHolder
from tkinter import Widget
from urllib import request
from allauth.account.forms import SignupForm
from django import forms
from django.forms import ModelForm
from petmatchaut.models import pet_perfil
from django.contrib.auth.forms import UserCreationForm

class petPerfilForm(ModelForm):
     class Meta:
         model = pet_perfil
         fields = ['pet_name', 'race', 'pet_age', 'pet_image', 'pet_owner']

         widgets = {
             'pet_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your pet name!'}),
             'race': forms.TextInput(attrs={'class': 'form-control'}),
             'pet_age': forms.NumberInput(attrs={'class': 'form-control'}),
             'pet_image': forms.FileInput(attrs={'class': 'form-control'}),
             'pet_owner': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'owner', 'type':'hidden'}),
         }

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


    