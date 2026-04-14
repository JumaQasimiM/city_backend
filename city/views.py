from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import City
from .serializers import CitySerializer

@api_view(['GET','POST'])
def city_list_create(request):
    if request.method == 'GET':
        city  = City.objects.all()
        serializer = CitySerializer(city, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='POST':
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
    elif request.method =='DELETE':
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
