from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . models import Place,PlaceComment,PlaceImage,PlaceLike,FavoratePlace
from serializers import PlaceSerializer,PlaceImageSerializer,PlaceLikeSerializer,PlaceCommentSerializer,FavoritePlaceSerializer





# create 
# list
# update
# delete
