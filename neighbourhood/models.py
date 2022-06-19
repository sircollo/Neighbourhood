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
  area_image = CloudinaryField('image', blank=True)
  def __str__(self):
    return self.name
  
  def create_neighbourhood(self):
    self.save()
    
  def delete_neighbourhood(self):
    self.delete()
  
  @classmethod
  def find_neighbourhood_by_id(cls, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    return neighbourhood
  
  @classmethod
  def update_neighbourhood(cls,name):
    neighbourhood = Neighbourhood.objects.get(name=name)
    neighbourhood.save()
    
  
  
class Profile(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  about = models.TextField()
  user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  picture = CloudinaryField('Avatar')
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self):
    return self.user.username
  
  def get_absolute_url(self):
    return reverse('index')
  
  def save_profile(self):
    self.save()
    
  def update_profile(self):
    self.update()
    
  def delete_profile(self):
    self.delete()

class Business(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField(max_length=50,unique=True)
  description = models.TextField(null=True)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  user = models.ForeignKey(Profile,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name