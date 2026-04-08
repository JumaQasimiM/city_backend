from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer


# list categories

@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many= True)
    return Response(serializer.data,status=200)

# create new category

@api_view(['POST'])
def create_category(request):
    pass
# update category
@api_view(['PUT'])
def update_category(request,pk):
    pass
# delete category

@api_view(['DELETE'])
def delete_category(request,pk):
    pass

# get one category --- category detail

@api_view(['GET'])
def category_detail(request,pk):
    category =get_object_or_404(Category,pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)