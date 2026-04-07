from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','name']
    def validate_name(self, value):
        value = value.strip() # remove space ' Germany '

        if len(value) < 4:
            raise serializers.ValidationError(
                'Country name must be at least 4 characters.'
            )
        if Country.objects.filter(name = value).exists():
            raise serializers.ValidationError('Country already exist!')

        return value