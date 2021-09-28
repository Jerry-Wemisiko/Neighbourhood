from django.db import models

# Create your models here.
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
