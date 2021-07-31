from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DescriptionModelSerializer,UserProfileModelSerializer
from .models import DescriptionModel,UserProfileModel
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from .models import *




class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer       

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileModelSerializer

class ListUser(APIView):
    def get(self,request):
        infos = DescriptionModel.objects.all()
        response = []
        for info in infos:
            all_info = {"Plant_Name":info.Plant_Name,"Price":info.price,"first_image":info.first_image.url,"second_image":info.second_image.url,"state":info.state,"city":info.city}
            response.append(all_info)

        return Response(data=response)    


class AddressView(ListAPIView):
    """
    you can filter object based on the city or state like:
    http://127.0.0.1:8000/description/youraddress/?city=Patna
    """
    serializer_class = DescriptionModelSerializer
    def get_queryset(self):
        queryset = DescriptionModel.objects.all()
        city_name = self.request.query_params.get('city')
        state_name = self.request.query_params.get('state')

        if city_name is not None:
            queryset = queryset.filter(city=city_name)
        if queryset.exists() is False:
            queryset = DescriptionModel.objects.all()
            queryset = queryset.filter(state = state_name)
             

    # if our_city:
    # queryset = queryset.filter(city="patna")
            
        return queryset


# def add_favourite(request,id):
#     description = get_object_or_404(DescriptionModel,id=id)
#     if description.favourite.filter(id=request.user.id).exists():
#         description.favourite.remove(request.user)
#     else:
#         description.favourite.add(request.user)

#     return HttpResponseRedirect(request.META['HTTP_REFERER'])



