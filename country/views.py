from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from.serializers import CountrySerializer






# REST method

'''
GET: list all countriew
POST: create new country
'''
@api_view(['GET','POST'])
def create_list_country(request):
    if request.method =='GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries,many =True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = CountrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'country created successfully.'},status=status.HTTP_201_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','DELETE','PATCH'])
def country_detail(request,pk):
    if request.method == 'GET':
        country = get_object_or_404(Country, pk = pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        country = get_object_or_404(Country,pk = pk)
        if country.cities.exists():
            return Response(
                {'error':'Can not delete country with existing city.'},
                status=status.HTTP_204_BAD_REQUEST
            )
        country.delete()
        return Response( {'success': 'country removed successfully'},status=status.HTTP_200_OK)   

    elif request.method == 'PATCH':
        country = get_object_or_404(Country,pk=pk)
        serializer = CountrySerializer(country, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Country updated successfully!','data':serializer.data},status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
