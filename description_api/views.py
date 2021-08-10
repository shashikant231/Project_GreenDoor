from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DescriptionModelSerializer,UserProfileModelSerializer
from .models import DescriptionModel,UserProfileModel
from rest_framework.generics import ListAPIView
from .models import *
from rest_framework.views import APIView
from rest_framework import filters




class DescriptionViewSet(viewsets.ModelViewSet):
    """
    Create New Description 

        Requeat Data : {
            "plant_name" : "name",
            "description" : "description",
            "price" : "price",
            "first_image" : "first_image",
            "second_image" : "second_image",
            "third_image" : "third_image",
            "fourth_image" : "fourth_image",
            "fifth_image" : "fifth_image",
            "state" : "state",
            "city" : "city",
            "user" : "user",
            "favourite" : "favourite"
        }

        Response : {
        "id": 8,
        "plant_name": "plant name",
        "description": "description for the plant",
        "price": price,
        "first_image": "image",
        "second_image": "image",
        "third_image": null,
        "fourth_image": null,
        "fifth_image": null,
        "state": "state",
        "city": "city",
        "user": "username",
        "favourite": []
    }
    """
    queryset = DescriptionModel.objects.all()
    serializer_class = DescriptionModelSerializer 
    filter_backends = [filters.SearchFilter]
    search_fields = ['plant_name'] 

        
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileModelSerializer


class ListUser(APIView):
    def get(self,request):
        infos = User.objects.all()
        response = []
        for info in infos:
            all_info = {"username":info.username,"email":info.email,"user_id":info.id}
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
            
        return queryset


# def add_favourite(request,id):
#     description = get_object_or_404(DescriptionModel,id=id)
#     if description.favourite.filter(id=request.user.id).exists():
#         description.favourite.remove(request.user)
#     else:
#         description.favourite.add(request.user)

#     return HttpResponseRedirect(request.META['HTTP_REFERER'])



