from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import super_type
from supers.models import Supers
from .serializers import SuperTypeSerializer
from .models import SuperType
from super_type import serializers


@api_view(['GET'])
def super_type_list(request):

    super_types = SuperType.objects.all()

    serializer = SuperTypeSerializer(super_types, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def super_type_detail(request, pk):
    try:
        super_type = SuperType.objects.get(pk=pk)
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data)

    except SuperType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
