from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else:
     messages.warning(request,'Password Mismatch')
      
  form = SignUpForm()
  return render(request=request, template_name='registration/register.html',context={'form':form})