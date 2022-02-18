from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def super_type_list(request):

    return Response('ok')
