from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views.generic.edit import View
# Create your views here.
def index(request):
  neighbourhoods = Neighbourhood.objects.all()
  context = {'neighbourhoods': neighbourhoods}
  return render(request, 'index.html', context)

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      firstname = form.cleaned_data['first_name']
      lastname = form.cleaned_data['last_name']
      phone_number = form.cleaned_data['phone_number']
      email = form.cleaned_data['email']
      user = User.objects.create_user(username,email=email, password=password)
      user.first_name = firstname 
      user.last_name = lastname  
      user.phone_number = phone_number
      user.save()
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

class SignOutView(View):
  def get(self,request):
    logout(request)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('index')
  
def profile(request,id):
  user = request.user
  profiles=Profile.objects.get(user=id)
  context = {'profile':profiles}
  return render(request, 'profiles.html', context)