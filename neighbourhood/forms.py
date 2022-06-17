from . import models
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Username'}), required=True)
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder':'Email'}), required=True)
    password1 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)
    password2 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}), required=True)
    
class SignInForm(AuthenticationForm): 
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
  class Meta:
    model = User
    fields = ['username','password']
    