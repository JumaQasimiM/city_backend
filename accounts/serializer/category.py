from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'places']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lazy import: اینجا import می‌کنیم تا circular import رخ ندهد
        from serializer.place import PlaceSerializer
        self.fields['places'] = PlaceSerializer(many=True, read_only=True)