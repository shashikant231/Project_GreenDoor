from .models import DescriptionModel
from rest_framework import serializers

class DescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = '__all__'