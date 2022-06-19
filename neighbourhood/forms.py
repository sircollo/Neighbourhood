from . import models
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='firstname', max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}), required=True)
    last_name = forms.CharField(label='lastname', max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}), required=True)
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}), required=True)
    phone_number = forms.IntegerField(label='phonenumber', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}), required=True)
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}), required=True)
    password1 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
    password2 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}), required=True)
    
class SignInForm(AuthenticationForm): 
  username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}), required=True)
  password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
  class Meta:
    model = User
    fields = ['username','password']
    