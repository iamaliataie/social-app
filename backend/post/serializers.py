from rest_framework import serializers

from .models import Post, Comment, Notification
from account.serializers import UserSerializer, FriendshipRequestSerializer


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
        fields = ['id', 'body', 'get_image', 'likes', 'comments', 'created_by', 'created_at_formatted']


class NotificationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    request = FriendshipRequestSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = ['id', 'body', 'post', 'request', 'created_by', 'created_at_formatted']