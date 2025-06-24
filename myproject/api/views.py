from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

#function to get data
@api_view(['GET'])
def get_data(request):
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    return Response(data)