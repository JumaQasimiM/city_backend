from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from.serializers import CountrySerializer


# list countries
@api_view(['GET'])
def county_list(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries,many =True)
    return Response(serializer.data)
    

# create new country
@api_view(['POST'])
def create_country(request):
    serializer = CountrySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success':'country created successfully.'},status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update the country
@api_view(['PATCH'])
def update_country(request,pk):
    pass
# delete the country
@api_view(['DELETE'])
def delete_country(request,pk):
    pass
# country detail
@api_view(['GET'])
def country_detail(request,pk):
    pass

