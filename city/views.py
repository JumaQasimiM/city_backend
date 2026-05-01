from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import City
from .serializers import CitySerializer
from helper.permission import IsAdminOrReadOnly


@api_view(["GET", "POST"])
@permission_classes([IsAdminOrReadOnly])
def city_list_create(request):

    # GET all cities
    if request.method == "GET":
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)

        return Response(serializer.data)

    # CREATE city
    serializer = CitySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "success": True,
            "message": "City created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAdminOrReadOnly])
def city_detail(request, pk):

    city = get_object_or_404(City, pk=pk)

    # GET
    if request.method == "GET":
        serializer = CitySerializer(city)
        return Response(serializer.data)

    # DELETE
    if request.method == "DELETE":
        city.delete()
        return Response({
            "success": True,
            "message": "City deleted"
        }, status=status.HTTP_204_NO_CONTENT)

    # UPDATE
    serializer = CitySerializer(city, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "success": True,
            "message": "City updated",
            "data": serializer.data
        })

    return Response({
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)