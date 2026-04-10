from django.urls import path
from . import views

urlpatterns =[
    path('',views.categories,name='category_list'),
    path('create',views.create_category),
    path('category_detail/<int:pk>/',views.category_detail),
    path('delete_category/<int:pk>/',views.delete_category),
    path('update_category/<int:pk>/',views.update_category)
    
]
