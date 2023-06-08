from rest_framework import serializers

from .models import Post, Comment
from account.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'body', 'created_by', 'created_at_formatted']

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['id', 'body', 'likes', 'comments', 'created_by', 'created_at_formatted']
        