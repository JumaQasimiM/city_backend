from rest_framework import serializers
from place.models import Place, Service, PlaceImage, PlaceComment, FavoratePlace, PlaceLike
from city.serializers import CitySerializer
from accounts.serializers import UserSerializer

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Service.objects.all()
    )
    services_detail = ServiceSerializer(source='services', many=True, read_only=True)
    city_detail = CitySerializer(source='city', read_only=True)
    owner_detail = UserSerializer(source='owner', read_only=True)

    class Meta:
        model = Place
        fields = '__all__'

class PlaceImageSerializer(serializers.ModelSerializer):
    place_detail = PlaceSerializer(source='place', read_only=True)
    class Meta:
        model = PlaceImage
        fields = '__all__'

class PlaceCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PlaceComment
        fields = '__all__'

class FavoritePlaceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = FavoratePlace
        fields = '__all__'

class PlaceLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PlaceLike
        fields = '__all__'