from django.db.models import fields
from .models import DescriptionModel,UserProfileModel
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