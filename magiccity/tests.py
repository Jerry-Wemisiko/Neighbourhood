from magiccity.models import Neighbourhood,Profile,Post,Business
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='jerry',password='1234')
        self.user.save()
        self.neighbourhood = Neighbourhood(name = "magiccity", location= "Miami", user= self.user, description='magiccity im the owner')
        self.neighbourhood.save_neighbourhood()
        self.profile = Profile(user = self.user,id_number=6898998,bio='this is where i came',email='j@gmail.com',  neighbourhood = self.neighbourhood)

   
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_get_profile(self):
        self.profile.save_profile()
        
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        saved_test = Profile.objects.all()
        self.assertTrue(len(saved_test) == 0)

class NeighbourhoodTest(TestCase):
 
    def setUp(self):
        self.user = User(username='jerry')
        self.user.save()
        self.neighbourhood = Neighbourhood(name = "magiccity", location= "Miami", user= self.user, description='magiccity im the owner')
        self.neighbourhood.create_neighbourhood()


    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_create_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        houses = Neighbourhood.objects.all()
        self.assertTrue(len(houses) > 0)

    def test_delete_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        houses = Neighbourhood.objects.all()
        self.assertTrue(len(houses) == 0)

class BusinessTest(TestCase):

    def setUp(self):

        self.user = User(username="j", password="pass123")
        self.user.save()
        self.neighbourhood = Neighbourhood(name = "magiccity", location= "Miami", user= self.user, description='magiccity im the owner')
        self.neighbourhood.save()
        self.business = Business(bizz_name='Where I came', email='jj@g.com',description='Entrepreneur')
     

   