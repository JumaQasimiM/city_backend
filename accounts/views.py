from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import User
from  . serializers import UserSerializer

from rest_framework import status


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data,status=200)
    
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_detail(request,pk):
    pass