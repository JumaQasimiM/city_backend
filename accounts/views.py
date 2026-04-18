from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import User
from  . serializers import UserSerializer
# Create your views here.


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data,status=200)
    
@api_view(['POST'])
def rigister_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('OK')
    return Response('no')