from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    # فقط نام یا id مکان‌ها را نشان می‌دهد
    # places = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # or
    # places = serializers.StringRelatedField(many=True)
    place_name = serializers.SerializerMethodField(method_name= 'get_place_name')

    # calculates and returns the count of related Place objects for each Category
    totle_place_per_category = serializers.SerializerMethodField(method_name='get_total_place_per_category')
    
    name = serializers.CharField(source = 'title')
    class Meta:
        model = Category
        fields = ['id', 'name','place_name','totle_place_per_category']
    
    def get_place_name(self,obj): # ojb = Place
        return [place.name for place in obj.places.all()]
    
    #
    def get_total_place_per_category(self,obj):
        return obj.places.count()