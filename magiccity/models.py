from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=200)
    neighbourhood_location = models.CharField(max_length=200)
    neighbourhood_description = models.TextField(max_length=500, blank=True)
    neighbourhood_photo = CloudinaryField('photo', default='img')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save()

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    def update_hood(self):
        neighbourhood_name = self.neighbourhood_name
        self.neighbourhood_name = neighbourhood_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
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

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)


class Business(models.Model):
    name = models.CharField(max_length=100,blank=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email= models.CharField(max_length=150,blank=True)
    description=models.TextField()

    def __str__(self) -> str:
        return self.name

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
        name = self.business_name
        self.business_name = name

class Post(models.Model):

    category = models.CharField(max_length=120)
    title = models.CharField(max_length=100, null=True)
    post = models.TextField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Post'    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()