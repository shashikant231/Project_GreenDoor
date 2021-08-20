from .models import DescriptionModel,UserProfileModel,Bookmark
from django.contrib.auth.models import User
from rest_framework import serializers


class DescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = '__all__'
    

    def to_representation(self, instance):
        res = super().to_representation(instance)
        image = UserProfileModel.objects.filter(user = instance.user.id).values('profile_pic')
        bio = UserProfileModel.objects.filter(user = instance.user.id).values('bio')
        email = User.objects.filter(username = instance.user.username).values('email')
        res['username'] = instance.user.username
        res['profile_pic'] = image[0]['profile_pic']
        res['user_email'] = email[0]['email']
        res['user_bio'] = bio[0]['bio']
        
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


class BookmarkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__' 