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
    # data_visualization = [item for item in super_types]  # for debugging
    serializer = SuperTypeSerializer(super_types, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def super_type_detail(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        data_visualization = [item for item in super_type]  # for debugging
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

#################################################################


# @api_view(['GET'])
# def super_type(request):

#     supers_param = request.query_params.get('supers')
#     sort_param = request.query_params.get('sort')

#     super_type = SuperType.objects.all()

#     print(supers_param)
#     print(sort_param)

#     # Truthy: if contains value then it is True
#     # if does not contain value then it is False
#     if supers_param:
#         supers = super_type.filter(super_type__name=supers_param)

#     if sort_param:
#         super_type = super_type.order_by(sort_param)

#     serializer = SuperTypeSerializer(supers, many=True)
#     return Response(serializer.data)
