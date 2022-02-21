from django.shortcuts import get_object_or_404
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


@api_view(['GET', 'PUT'])
def super_type_detail(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
