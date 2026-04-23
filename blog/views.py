# from django.shortcuts import render

# # Create your views here.
#     # muss in der view schreiben.
# def perform_create(self, serializer):
#     serializer.save(user=self.request.user)


from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers

class BlogViewSet(ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
