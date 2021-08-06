from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register("model",DescriptionViewSet)
router.register("profile",UserProfileViewSet)




urlpatterns = [
        path("youraddress/",AddressView.as_view()),
        # path("add_favourite/<id>",add_favourite)
        ] + router.urls

    
