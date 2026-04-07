from rest_framework import serializers
from .models import City, CityImage

from country.models import Country
from country.serializers import CountrySerializer

class CitySerializer(serializers.ModelSerializer):
    # ?!
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all()
    )
    country_detail = CountrySerializer(source='country', read_only=True)

    class Meta:
        model = City
        fields = '__all__'
    
class CityImageSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all()
    )
    city_detail = CitySerializer(source='city', read_only=True)

    class Meta:
        model = CityImage
        fields = ['id', 'city', 'city_detail', 'image']