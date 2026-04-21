from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns  =[
    path('',views.users),
    path('register/',views.register_user),
    path('<int:pk>/',views.user_detail),
    # login
    path('login/', views.LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]