from django.urls import path
from . import views

urlpatterns =[
    path('',views.categories,name='category_list'),
    # path('create_category/',views.create,name='category_create'),
    
]
