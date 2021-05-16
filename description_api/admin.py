from django.contrib import admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.contrib.auth.models import User
from .models import DescriptionModel,UserProfileModel

# Register your models here.
admin.site.register(DescriptionModel)
admin.site.register(UserProfileModel)
