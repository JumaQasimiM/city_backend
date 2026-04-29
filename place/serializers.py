from rest_framework import serializers
from . import models

from category.models import Category
from category.serializers import CategorySerializer

from accounts.models import User
from accounts.serializers import UserSerializer

from city.models import City
from city.serializers import CitySerializer


# 🔹 Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

# 🔹 Place Image
class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaceImage
        fields = '__all__'

# 🔹 Place
class PlaceSerializer(serializers.ModelSerializer):
    # write (POST)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    city = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all()
    )
    owner = serializers.ReadOnlyField(source="owner.id")
    services = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Service.objects.all()
    )

    # read (GET)
    category_detail = CategorySerializer(source='category', read_only=True)
    city_detail = CitySerializer(source='city', read_only=True)
    owner_detail = UserSerializer(source='owner', read_only=True)
    services_detail = ServiceSerializer(source='services', many=True, read_only=True)

    images = PlaceImageSerializer(many=True, read_only=True)
    class Meta:
        model = models.Place
        fields = '__all__'




# 🔹 Comment
class PlaceCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.PlaceComment
        fields = '__all__'


# 🔹 Favorite
class FavoritePlaceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.FavoratePlace
        fields = '__all__'


# 🔹 Like
class PlaceLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.PlaceLike
        fields = '__all__'