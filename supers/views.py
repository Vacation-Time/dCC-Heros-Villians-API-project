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
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


##################################################


# @api_view(['GET'])
# def supers_list(request):

#     super_type_param = request.query_params.get('super_type')
#     sort_param = request.query_params.get('sort')

#     supers = SuperType.objects.all()

#     # Truthy: if contains value then it is True
#     # if does not contain value then it is False
#     if super_type_param:
#         supers = supers.filter(supers_name=super_type_param)

#     if sort_param:
#         supers = supers.order_by(sort_param)

#     serializer = SupersSerializer(supers, many=True)
#     return Response(serializer.data)
