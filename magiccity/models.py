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

class Post(models.Model):
    POST_CHOICES = (
        ('1', 'Security'),
        ('2', 'Health Emergency'),
        ('3', 'Entertainment'),
        ('4', 'Fire Breakouts'),
        ('5', 'Playground'),
        ('6', 'Death'),
        ('7', 'Gym'),
    )
    category = models.CharField(max_length=120, choices=POST_CHOICES)
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Post'    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()