from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import super_type
from supers.models import Supers
from .serializers import SuperTypeSerializer
from .models import SuperType
from super_type import serializers


@api_view(['GET', 'POST'])
def super_type_list(request):
    if request.method == 'GET':
        super_type = SuperType.objects.all()
        # data_visualization = [item for item in supers]  # for debugging
        serializer = SuperTypeSerializer(super_type, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_type_detail(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        # data_visualization = [item for item in super_type]  # for debugging
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
