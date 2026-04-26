from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser,FormParser

from . models import Place,PlaceComment,PlaceImage,PlaceLike,FavoratePlace,Service
from . serializers import PlaceSerializer,PlaceImageSerializer,ServiceSerializer,PlaceLikeSerializer,PlaceCommentSerializer,FavoritePlaceSerializer

# filter and search 
from django_filters.rest_framework import DjangoFilterBackend


# services

class ServiceViewSet(ModelViewSet):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer

class PlaceViewSet(ModelViewSet):
   queryset = Place.objects.all()
   serializer_class = PlaceSerializer

   # filter and search with django filter - library
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['city', 'category']

   '''
   /places?city=1
   /places?category=2
   /places?city=1&category=2
   '''

   # def get_queryset(self):
   #      queryset = Place.objects.all()

   #      city = self.request.query_params.get('city')
   #      category = self.request.query_params.get('category')

   #      if city:
   #          queryset = queryset.filter(city_id=city)

   #      if category:
   #          queryset = queryset.filter(category_id=category)

   #      return queryset

class PlaceImageViewSet(ModelViewSet):
   queryset = PlaceImage.objects.all()
   serializer_class = PlaceImageSerializer
   parser_classes = [MultiPartParser,FormParser]
