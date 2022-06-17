from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from neighbourhood.models import *
# Create your models here.
class Neighbourhood(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  occupants = models.IntegerField(default=0)
  admin = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='neighbour')
  health_contact = models.IntegerField(null=True)
  police_contact = models.IntegerField(null=True)
  
  def __str__(self):
    return self.name
  
  
class Profile(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  about = models.TextField()
  user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  picture = CloudinaryField('Profiles')
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self):
    return self.user.username
  
  def get_absolute_url(self):
    return reverse('index')

