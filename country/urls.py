
from django.urls import path
from . import views

urlpatterns = [
    path('',views.county_list),
    path('create/',views.create_country),
]