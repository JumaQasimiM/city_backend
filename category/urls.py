from django.urls import path
from . import views

urlpatterns =[
    path('',views.categories,name='category_list'),
    path('category_detail/<int:pk>/',views.category_detail)
    
]
