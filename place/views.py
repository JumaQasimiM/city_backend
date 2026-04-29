from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import IsAuthenticated

from . models import Place,PlaceComment,PlaceImage,PlaceLike,FavoratePlace,Service
from . serializers import PlaceSerializer,PlaceImageSerializer,ServiceSerializer,PlaceLikeSerializer,PlaceCommentSerializer,FavoritePlaceSerializer

# filter and search 
from django_filters.rest_framework import DjangoFilterBackend


# chart 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from django.db.models import Count


# services

class ServiceViewSet(ModelViewSet):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer

class PlaceViewSet(ModelViewSet):
   queryset = Place.objects.all()
   serializer_class = PlaceSerializer
   def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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

class PlaceGrowthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        period = request.GET.get("period", "month")  

        queryset = Place.objects.all()

        # role filter
        if user.role == "business":
            queryset = queryset.filter(owner=user)

        #  grouping
        if period == "day":
            trunc = TruncDay("register_date")
        elif period == "week":
            trunc = TruncWeek("register_date")
        else:
            trunc = TruncMonth("register_date")

        data = (
            queryset
            .annotate(date=trunc)
            .values("date")
            .annotate(count=Count("id"))
            .order_by("date")
        )

        return Response(data)