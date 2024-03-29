from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import super_type
from super_type.models import SuperType
import supers
from .serializers import SupersSerializer
from .models import Supers
from supers import serializers


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        # data_visualization = [item for item in supers]  # for debugging
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        # data_visualization = [item for item in super]  # for debugging
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##################################################


@api_view(['GET'])
def supers_list(request):

    super_type_param = request.query_params.get('type')

    supers = Supers.objects.all()

    # print(super_type_param)
    # print(sort_param)

    # Truthy: if contains value then it is True
    # if does not contain value then it is False
    if super_type_param == 'hero':
        heroes = supers.filter(super_type__type='Hero')
        serializer = SupersSerializer(heroes, many=True)
        return Response(serializer.data)
    elif super_type_param == 'villain':
        villains = supers.filter(super_type__type='Villain')
        serializer = SupersSerializer(villains, many=True)
        return Response(serializer.data)
    elif super_type_param == 'something_inbetween':
        something_inbetween = supers.filter(
            super_type__type='Something In-Between')
        serializer = SupersSerializer(something_inbetween, many=True)
        return Response(serializer.data)
    else:

        # data_visualization = [item for item in supers_list]  # for debugging
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)
