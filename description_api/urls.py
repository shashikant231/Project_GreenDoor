from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register("model",DescriptionViewSet)
router.register("",UserProfileViewSet)




urlpatterns = [
    # path("model/",DescriptionViewSet.as_view({"get": "list"})),
      path ("",include(router.urls))
    ]
