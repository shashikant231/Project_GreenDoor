from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register("model",DescriptionViewSet)
router.register("",UserProfileViewSet)




urlpatterns = [
        path("name/",ListUser.as_view()),
        path ("",include(router.urls)),
    ]
