from django.contrib import admin
from django.contrib.auth.models import User
from .models import DescriptionModel,UserProfileModel

class Filter(admin.ModelAdmin):
    list_display = ("plant_name","price")
    list_filter = ("plant_name","user")
    search_fields = ('plant_name',)

# Register your models here.
admin.site.register(DescriptionModel,Filter)
admin.site.register(UserProfileModel)

