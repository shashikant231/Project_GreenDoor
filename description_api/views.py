from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DescriptionModelSerializer,UserProfileModelSerializer
from .models import DescriptionModel,UserProfileModel
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import *




class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer

# @api_view(['POST',])
# def description_view(request):
#     if request.method == 'POST':
#         serializer = DescriptionModelSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = "successfully added a new model"
#         else:
#             data = serializer.error()
#         return Response(data)        

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




