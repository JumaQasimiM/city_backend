
from django.urls import path
from . import views

'''
REST : METHOD 
'''
urlpatterns = [
    path('',views.create_list_country),
    path('<int:pk>/',views.country_detail),
]