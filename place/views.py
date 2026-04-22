from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser,FormParser

from . models import Place,PlaceComment,PlaceImage,PlaceLike,FavoratePlace
from . serializers import PlaceSerializer,PlaceImageSerializer,PlaceLikeSerializer,PlaceCommentSerializer,FavoritePlaceSerializer





class PlaceViewSet(ModelViewSet):
   queryset = Place.objects.all()
   serializer_class = PlaceSerializer

class PlaceImageViewSet(ModelViewSet):
   queryset = PlaceImage.objects.all()
   serializer_class = PlaceImageSerializer
   parser_classes = [MultiPartParser,FormParser]