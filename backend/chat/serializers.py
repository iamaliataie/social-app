from rest_framework import serializers

from .models import Conversation, ConversationMessage
from account.serializers import UserSerializer

class CoversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Conversation
        fields = ['id', 'users', 'modified_at_formatted']


class ConversationMessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    received_by = UserSerializer(read_only=True)
    
    class Meta:
        model = ConversationMessage
        fields = ['id', 'body', 'created_by', 'received_by', 'created_at_formatted']
    

class CoversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)
    
    class Meta:
        model = Conversation
        fields = ['id', 'users', 'modified_at_formatted', 'messages']