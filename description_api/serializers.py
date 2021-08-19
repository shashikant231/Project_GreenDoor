from .models import DescriptionModel,UserProfileModel
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfileModel

class DescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = '__all__'
    

    def to_representation(self, instance):
        res = super().to_representation(instance)
        image = UserProfileModel.objects.filter(user = instance.user.id).values('profile_pic')
        res['username'] = instance.user.username
        res['image'] = image
        return res

 

class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'   

    def to_representation(self, instance):
        res = super().to_representation(instance)
        email = User.objects.filter(username = instance.user.username).values('email')
        res['email'] = email[0]['email']
        res['username'] = instance.user.username
        return res      