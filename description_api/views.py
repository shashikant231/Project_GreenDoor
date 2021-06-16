from django.http.response import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DescriptionModelSerializer,UserProfileModelSerializer
from .models import DescriptionModel,UserProfileModel
from rest_framework.views import APIView
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


