from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    totale_city = serializers.SerializerMethodField(method_name='get_city_per_country' )
    class Meta:
        model = Country
        fields = ['id','name','totale_city']
    def validate_name(self, value):
        value = value.strip() # remove space ' Germany '

        if len(value) < 4:
            raise serializers.ValidationError(
                'Country name must be at least 4 characters.'
            )
        if Country.objects.filter(name__iexact = value).exists():
            raise serializers.ValidationError('Country already exist!')

        return value
    def get_city_per_country(self, obj):
        return obj.cities.count()