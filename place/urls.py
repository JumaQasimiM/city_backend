from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import PlaceGrowthView

router = DefaultRouter()
router.register('places', views.PlaceViewSet)
router.register('services', views.ServiceViewSet)
router.register('placeComments', views.PlaceCommentViewSet)

urlpatterns = [
    path("places/growth/", PlaceGrowthView.as_view()),
]


urlpatterns += router.urls