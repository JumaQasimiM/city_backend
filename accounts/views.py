from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import User
from  . serializers import UserSerializer

from rest_framework import status

# jwt login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    pass


# get all users
@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data,status=200)
    
# register  a new user / create a new account
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update , delete and get a user
@api_view(['GET','DELETE','PATCH'])
def user_detail(request,pk):
    # get a user 
    user = get_object_or_404(User,pk=pk)

    # ------- GET: get single user -----------
    if request.method =='GET':
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
     # ------- DELETE: remove user -----------
    elif request.method == 'DELETE':
        user.delete()
        return Response({
            'success': True,
            'message': 'User removed successfully.'
        },
        status=status.HTTP_204_NO_CONTENT)
    
     # ------- PATCH: update a user -----------
    elif request.method =='PATCH':
        serializer = UserSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'message': 'User updated successfully.',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'success': False,
                'message': 'Validation error',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

# login user

# logout user
    


