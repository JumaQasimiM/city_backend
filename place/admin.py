from django.contrib import admin

# Register your models here.

from .models import Place,PlaceImage,FavoratePlace,PlaceComment,PlaceLike,Service

admin.site.register(Place)
admin.site.register(PlaceImage)
admin.site.register(FavoratePlace)
admin.site.register(PlaceComment)
admin.site.register(PlaceLike)
admin.site.register(Service)