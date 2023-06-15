from rest_framework import serializers
from .models import User, FriendshipRequest

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'friends', 'posts', 'get_avatar']


class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    received_by = UserSerializer(read_only=True)
    
    class Meta:
        model = FriendshipRequest
        fields = ['id', 'created_by', 'received_by',]