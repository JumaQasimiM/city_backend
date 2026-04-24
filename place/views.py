from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser,FormParser

from . models import Place,PlaceComment,PlaceImage,PlaceLike,FavoratePlace,Service
from . serializers import PlaceSerializer,PlaceImageSerializer,ServiceSerializer,PlaceLikeSerializer,PlaceCommentSerializer,FavoritePlaceSerializer



# services

class ServiceViewSet(ModelViewSet):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer

class PlaceViewSet(ModelViewSet):
   queryset = Place.objects.all()
   serializer_class = PlaceSerializer

class PlaceImageViewSet(ModelViewSet):
   queryset = PlaceImage.objects.all()
   serializer_class = PlaceImageSerializer
   parser_classes = [MultiPartParser,FormParser]
