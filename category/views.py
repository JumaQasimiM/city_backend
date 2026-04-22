# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Category
# from .serializers import CategorySerializer

# """
# Category API (using api_view for learning DRF)

# Endpoints:
# 1. categories          -> list all categories
# 2. create_category     -> create a new category
# 3. update_category     -> update an existing category
# 4. delete_category     -> delete a category
# 5. category_detail     -> retrieve a single category
# """

# # GET: get all categories

# @api_view(['GET'])
# def categories(request):
#     categories = Category.objects.all()
#     serializer = CategorySerializer(categories,many= True)
#     return Response(serializer.data,status=status.HTTP_200_OK)

# # POST: create new category
# @api_view(['POST']) 
# def create_category(request):
#     serializer = CategorySerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         # return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'success','New Category create successfully!'})
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # PATCH: update category
# @api_view(['PATCH','PUT'])
# def update_category(request,pk):
#     category  = get_object_or_404(Category,pk=pk)
#     serializer = CategorySerializer(category,data = request.data,partial=True )
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # DELETE: delete category

# @api_view(['DELETE'])
# def delete_category(request,pk):
#     category  = get_object_or_404(Category,pk=pk)
#     if category.places.exists():
#         return Response(
#             {'error':'Can not delete category with existing place.'},
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     category.delete()
#     return Response( {'message': 'category removed successfully'},status=status.HTTP_200_OK)   

# # GET: retrieve a single category --- category detail

# @api_view(['GET'])
# def category_detail(request,pk):
#     category =get_object_or_404(Category,pk=pk)
#     serializer = CategorySerializer(category)
#     return Response(serializer.data,status=status.HTTP_200_OK)



# with viewset
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer