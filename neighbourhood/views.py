from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views.generic.edit import View
from django.views.generic import ListView
from django.db.models import Q
from .email import send_welcome_email
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
      name = (firstname + ' ' + lastname)
      send_welcome_email(name,email)
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
    form = PostBusinessForm(request.POST,request.FILES)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      description = form.cleaned_data['description']
      poster = form.cleaned_data['poster']
      business = Business(name=name,email=email, description=description,user=profiles,poster=poster)
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

def neighbourhoods(request):
  neighbourhoods = Neighbourhood.objects.all()
  context = {'neighbourhoods':neighbourhoods}
  return render(request, 'neighbourhoods.html', context)

# class search_business(ListView):
#   model= Business
#   template_name = 'business_list.html'
  

#   def search_business(request):
#     query = request.GET.get('search_business')
#     businesses = Business.objects.filter(
#       Q(name__icontains=query)
    
#     )
#     # if not search_user
#     return businesses
def search(request):
    query  = request.GET.get('search_business')
    if not query :
      query = ""
    businesses = Business.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'business_list.html', {'businesses': businesses})
  
def user_business(request,id):
  profiles=Profile.objects.get(user=id)
  businesses = Business.objects.filter(user=profiles)
  return render(request, 'user_business_list.html', {'businesses': businesses})


def create_post(request):
  user = request.user
  profiles = Profile.objects.get(user=user)
  # neighbourhood = Neighbourhood.objects.get(name=profiles)
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data['title']
      message = form.cleaned_data['message']
      new_post =Post(title=title,message=message,user=profiles)
      new_post.save()
      return redirect('index')
  form = PostForm()
  return render(request, 'post_form.html',{'form': form})

def postList(request):
  posts = Post.objects.all()
  return render(request, 'posts.html',{'posts': posts})
  