

from rest_framework.response import Response
from rest_framework.decorators import api_view



from .serializers import DescriptionModelSerializer


@api_view(['POST',])
def description_view(request):
    if request.method == 'POST':
        serializer = DescriptionModelSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "successfully added a new model"
        else:
            data = serializer.error()
        return Response(data)        