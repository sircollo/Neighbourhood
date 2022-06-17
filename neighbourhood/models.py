from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from neighbourhood.models import *
# Create your models here.

class Profile(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  about = models.TextField()
  user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  picture = CloudinaryField('Profiles')
  
  def __str__(self):
    return self.user.username
  
  def get_absolute_url(self):
    return reverse('index')
  