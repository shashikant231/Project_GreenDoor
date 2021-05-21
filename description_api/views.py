

from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DescriptionModelSerializer,UserProfileModelSerializer
from .models import DescriptionModel,UserProfileModel


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