from django.urls import path
from django.urls.resolvers import URLPattern
from .views import description_view


app_name  = 'account'
urlpatterns = [
    path('',description_view,name="register"),
    ]
