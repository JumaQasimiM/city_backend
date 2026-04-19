from django.urls import path
from . import views

urlpatterns  =[
    path('',views.users),
    path('register/',views.register_user),
    path('<int:pk>/',views.user_detail)
]