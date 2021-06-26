from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class DescriptionModel(models.Model):
    user = models.ForeignKey(User, null=False, on_delete= models.CASCADE)
    Plant_Name = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True)
    first_image = models.ImageField(upload_to ='media/')
    second_image = models.ImageField(upload_to ='media/')
    third_image = models.ImageField(upload_to ='media/')
    fourth_image = models.ImageField(upload_to ='media/')
    fifth_image = models.ImageField(upload_to ='media/')
    #location
    state = models.CharField(max_length=50,null=False,default='Bihar')
    city = models.CharField(max_length=80,null=False,default='Patna')

    def __str__(self):
        return self.Plant_Name


class UserProfileModel(models.Model):
    user = models.OneToOneField(User,null=False,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='media/')
    bio = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)	
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username