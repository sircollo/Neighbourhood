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
  businesses = Business.objects.filter(user=profiles)
  context = {'profile':profiles,'businesses':businesses}
  return render(request, 'profiles.html', context)

def businesspost(request,id):
  profiles=Profile.objects.get(user=id)
  # neighbourhood = Neighbourhood.objects.get(profile=id)
  users = Business.objects.filter(user=profiles)
  if request.method == 'POST':
    form = PostBusinessForm(data=request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      description = form.cleaned_data['description']
      business = Business(name=name,email=email, description=description,user=profiles)
      business.save()
      # form.save()
      return redirect('profile',id)
    else:
     messages.warning(request,'Incorrect Information')
      
  form = PostBusinessForm()
  context = {'form': form, 'profile': profiles,'messages': messages}
  return render(request, 'post_business.html',context)

def business(request):
  business = Business.objects.all()
  context = {'businesses':business}
  return render(request, 'businesses.html', context)
  