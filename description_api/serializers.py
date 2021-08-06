from django.db.models import fields
from .models import DescriptionModel,UserProfileModel
from rest_framework import serializers

class DescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['user'] = instance.user.username
        return res

class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'         