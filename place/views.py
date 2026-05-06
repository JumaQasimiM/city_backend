from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from django.db.models import Count

from .models import (
    Place,
    PlaceComment,
    PlaceImage,
    PlaceLike,
    FavoratePlace,
    Service,
)

from .serializers import (
    PlaceSerializer,
    PlaceImageSerializer,
    ServiceSerializer,
    PlaceLikeSerializer,
    PlaceCommentSerializer,
    FavoritePlaceSerializer,
)

from helper.permission import IsAdminOrReadOnly, IsAdminBusinessOrReadOnly


# =========================
#  SERVICE
# =========================
class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]


# =========================
#  PLACE
# =========================
class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAdminBusinessOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["city", "category"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# =========================
#  COMMENTS
# =========================
class PlaceCommentViewSet(ModelViewSet):
    queryset = PlaceComment.objects.all()
    serializer_class = PlaceCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["place"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# =========================
#  GROWTH CHART API
# =========================
class PlaceGrowthView(APIView):
    permission_classes = [IsAdminBusinessOrReadOnly]

    def get(self, request):
        user = request.user
        period = request.GET.get("period", "month")

        
        queryset = Place.objects.all()

        # role
        if user.role == "business":
            queryset = queryset.filter(owner=user)

        #  grouping
        if period == "day":
            trunc = TruncDay("register_date")
        elif period == "week":
            trunc = TruncWeek("register_date")
        else:
            trunc = TruncMonth("register_date")

        #  aggregation
        data = (
            queryset
            .annotate(date=trunc)
            .values("date")
            .annotate(count=Count("id"))
            .order_by("date")
        )

        return Response(data)