from django.db.models import fields
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title","author","content")
