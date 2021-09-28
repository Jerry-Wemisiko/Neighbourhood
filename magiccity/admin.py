from magiccity.models import Business, Neighbourhood, Post, Profile
from django.contrib import admin
from django.db import models
from magiccity.models import Profile,Neighbourhood,Business,Post
# Register your models here.

admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)