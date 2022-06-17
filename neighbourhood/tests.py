from django.test import TestCase
from .models import *
# Create your tests here.

class TestNeighbourHoodCase(TestCase):
  def setUp(self):
    self.admin = Profile(first_name='collo')
    self.admin.save()
    self.neighbourhood = Neighbourhood(id="1",name='korogocho',location='ngata',occupants="1",health_contact=12345,police_contact=54321,admin=self.admin)
    
  def test_instance(self):
    self.assertTrue(self.neighbourhood,Neighbourhood)
    
  # def tearDown(self):
  #   Neighbourhood.objects.delete()
    
  def test_create_neigborhood(self):
    self.neighbourhood.create_neighbourhood()
    new_neigborhood = Neighbourhood.objects.all()
    self.assertTrue(len(new_neigborhood)>0)
    
  def test_delete_neighbourhood(self):
    self.neighbourhood.delete_neighbourhood()
    new_neigborhood =Neighbourhood.objects.filter(admin=self.admin)
    self.assertTrue(len(new_neigborhood) == 0)
    
  def test_find_neighbourhood_by_id(self):
    self.neighbourhood.create_neighbourhood()    
    found_neighbouhood = Neighbourhood.find_neighbourhood_by_id("1")
    self.assertTrue(found_neighbouhood.name == "korogocho")
    
  def test_update_neighbourhood(self):
    self.neighbourhood.create_neighbourhood()
    new_neigborhood = Neighbourhood.objects.get(name='korogocho')
    self.neighbourhood.update_neighbourhood(new_neigborhood)
    
    
  