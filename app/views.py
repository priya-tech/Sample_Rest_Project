from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def UserList(request):
    if request.method == 'GET':
        data = UserModel.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
        # if not serializer.is_valid():
        #     return Response(serializer.data)
        
@api_view(['POST'])
def CreateUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def UserDetail(request, pk):
    try:
        user_data = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user_data)
        return Response(serializer.data)

        # if serializer.is_valid():
        #     return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UserSerializer(user_data, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

