from rest_framework import serializers
from . import models 
from category.models import Category
from category.serializers import CategorySerializer
from accounts.models import User
from accounts.serializers import UserSerializer
from city.models import City
from city.serializers import CitySerializer


class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Place
        fields = '__all__'

class PlaceImageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaceImage
        fields = '__all__'
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class PlaceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaceComment
        fields = '__all__'

class FavoratePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoratePlace
        fields = '__all__'

class PlaceLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaceLike
        fields = '__all__'