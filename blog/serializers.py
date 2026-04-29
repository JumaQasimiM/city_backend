from rest_framework import serializers
from .models import Blog, BlogComment
from accounts.serializers import UserSerializer

class BlogCommentSerializer(serializers.ModelSerializer):
    """
    read_only: fields are returned in the API response,
    but cannot be set or modified by the user.
    """
    user = UserSerializer(read_only=True)
    blog = serializers.PrimaryKeyRelatedField(read_only=True) 

    class Meta:
        model = BlogComment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)  # related_name='comments' -- in model
    user = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'