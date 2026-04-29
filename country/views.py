from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Country
from .serializers import CountrySerializer

"""
Country API (DRF - function based views)

This API provides basic CRUD operations for Country model.

Endpoints:
--------------------------------------------------
GET     /countries/          -> List all countries
POST    /countries/          -> Create a new country

GET     /countries/<id>/     -> Retrieve a single country
PATCH   /countries/<id>/     -> Partially update a country
DELETE  /countries/<id>/     -> Delete a country (if no related cities)
--------------------------------------------------
"""


# ==============================
# LIST & CREATE
# ==============================
"""
GET  : return all countries
POST : create a new country
"""
@api_view(['GET', 'POST'])
def create_list_country(request):

    # ---------- GET ----------
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    # ---------- POST ----------
    elif request.method == 'POST':
        #  check login
        if not request.user.is_authenticated:
            return Response({"message": "Login required"}, status=401)

        #  only admin
        if request.user.role != "admin":
            return Response({"message": "Permission denied"}, status=403)

        serializer = CountrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Country created", "data": serializer.data},
                status=201
            )

        return Response(serializer.errors, status=400)
# ==============================
# DETAIL / UPDATE / DELETE
# ==============================
"""
GET    : retrieve a single country
PATCH  : update country partially
DELETE : delete country (only if no related cities)
"""
@api_view(['GET', 'PATCH', 'DELETE'])
def country_detail(request, pk):

    country = get_object_or_404(Country, pk=pk)

    # ---------- GET ----------
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    #  check login for protected actions
    if not request.user.is_authenticated:
        return Response({"message": "Login required"}, status=401)

    #  admin
    if request.user.role != "admin":
        return Response({"message": "Permission denied"}, status=403)

    # ---------- DELETE ----------
    if request.method == 'DELETE':
        if country.cities.exists():
            return Response(
                {"message": "Cannot delete country with cities"},
                status=400
            )

        country.delete()
        return Response({"message": "Deleted"}, status=204)

    # ---------- PATCH ----------
    if request.method == 'PATCH':
        serializer = CountrySerializer(country, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Updated", "data": serializer.data}
            )

        return Response(serializer.errors, status=400)

    # get object or return 404
    country = get_object_or_404(Country, pk=pk)

    # ---------- GET: retrieve ----------
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------- DELETE ----------
    elif request.method == 'DELETE':
        # prevent delete if related cities exist
        if country.cities.exists():
            return Response(
                {
                    'success': False,
                    'message': 'Cannot delete country with existing cities.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        country.delete()
        return Response(
            {
                'success': True,
                'message': 'Country removed successfully.'
            },
            status=status.HTTP_204_NO_CONTENT
        )

    # ---------- PATCH: partial update ----------
    elif request.method == 'PATCH':
        serializer = CountrySerializer(
            country,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'message': 'Country updated successfully.',
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