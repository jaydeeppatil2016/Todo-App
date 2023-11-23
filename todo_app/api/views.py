from django.shortcuts import render
from rest_framework import viewsets
from api.models import todo_task
from api.serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer  # Import your serializer
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = todo_task.objects.all()
    serializer_class =TodoSerializer


    # views.py
@api_view(['POST'])
def create_data(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
