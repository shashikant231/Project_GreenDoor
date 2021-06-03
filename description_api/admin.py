from django.contrib import admin
from django.contrib.auth.models import User
from .models import DescriptionModel,UserProfileModel

class Filter(admin.ModelAdmin):
    list_display = ("Plant_Name","price")
    list_filter = ("Plant_Name","user")
    search_fields = ('Plant_Name',)

# Register your models here.
admin.site.register(DescriptionModel,Filter)
admin.site.register(UserProfileModel)
