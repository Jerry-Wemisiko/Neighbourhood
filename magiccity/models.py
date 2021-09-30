from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighbourhood(models.Model):
    house_name = models.CharField(max_length=50)
    house_location = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.house_name

    def create_neighbourhood(self):
        self.save()

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_house(cls, house_id):
        return cls.objects.filter(id=house_id)

    def update_occupants(self):
        name = self.name
        self.name = name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


    def save_profile(self):
        self.save()


    def delete_profile(self):
        self.delete()


class Business(models.Model):
    bizz_name = models.CharField(max_length=100,blank=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email= models.CharField(max_length=150,blank=True)
    description=models.TextField()

    def __str__(self) -> str:
        return self.bizz_name

    def save_business(self):
        self.save()

    def new_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id = business_id)
        return business

    @classmethod
    def search_by_name(cls,search_term):
    	bizz = cls.objects.filter(name__icontains=search_term)
    	return bizz

    def update_business(self):
        name = self.bizz_name
        self.bizz_name = name

class Post(models.Model):

    category = models.CharField(max_length=120)
    title = models.CharField(max_length=100, null=True)
    post = models.TextField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()