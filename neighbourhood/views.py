from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import *
# Create your views here.
def index(request):
  neighbourhoods = Neighbourhood.objects.all()
  context = {'neighbourhoods': neighbourhoods}
  return render(request, 'index.html', context)

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('signin')
    else:
     messages.warning(request,'Password Mismatch')
      
  form = SignUpForm()
  return render(request=request, template_name='registration/register.html',context={'form':form})

def signin(request):
  if request.method == 'POST':
    form = SignInForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username,password=password)
      if user is not None:
        login(request,user)
        return redirect('index')
      else:
        messages.error(request,'Invalid username or password')
        
    else:
      messages.error(request,'Invalid username or password')
  form = SignInForm()
  return render(request,'registration/login.html',{'form':form})