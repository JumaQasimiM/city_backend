from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# for auth and permission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import City
from .serializers import CitySerializer


"""
City API (DRF - function based views)

This API provides basic CRUD operations for City model.

Endpoints:
--------------------------------------------------
GET     /cities/          -> List all cities
POST    /cities/          -> Create a new cities

GET     /cities/<id>/     -> Retrieve a single cities
PATCH   /cities/<id>/     -> Partially update a cities
DELETE  /cities/<id>/     -> Delete a cities (if no related Places)
--------------------------------------------------
"""

@api_view(['GET','POST'])
def city_list_create(request):
    # ---------- GET : retrieve single City --------------
    if request.method == 'GET':
        city  = City.objects.all()
        serializer = CitySerializer(city, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # ---------- POST : create new City-------------- 
    elif request.method =='POST':
        # jast admin allow to create a city
        if request.user.role != "admin":
            return Response(
                    {"message": "Permission denied"},
                    status=status.HTTP_403_FORBIDDEN
                )

        serializer = CitySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'message': 'City created successfully.',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'success': False,
                'message': 'Validation error',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET','DELETE','PATCH'])
def city_detail(request,pk):
    city = get_object_or_404(City, pk=pk)
    # ------- GET : retrieve single city ------
    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # -------- DELETE : remove a city --------------
    elif request.method =='DELETE':
        # ----- if related place on this city exists ------
        if city.places.exists():
            return Response(
                            {
                                'success': False,
                                'message': 'Cannot delete City with existing place.'
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
        city.delete()
        return Response(
            {
                'success': True,
                'message': 'City removed successfully.'
            },
            status=status.HTTP_204_NO_CONTENT
        )
    # ---------- PATCH : update the city ------------
    elif request.method =='PATCH':
        serializer = CitySerializer(city, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'message': 'City updated successfully.',
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
