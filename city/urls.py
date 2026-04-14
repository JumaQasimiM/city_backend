from django.urls import path
from . import views

urlpatterns =[
    path('',views.city_list_create),
    path('<int:pk>/',views.city_detail)
]