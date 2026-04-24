
from place import views
from rest_framework.routers import DefaultRouter

# create instance of defaultrouter
router = DefaultRouter() 
router.register('',views.ServiceViewSet)

urlpatterns  = router.urls