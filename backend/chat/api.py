from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Conversation, ConversationMessage
from .serializers import CoversationSerializer, ConversationMessageSerializer, CoversationDetailSerializer
from account.models import User
from django.utils import timezone


@api_view(['GET'])
def get_conversations(request):
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    serializer = CoversationSerializer(conversations, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_active_conversation(request, conversation_id):
    converation = Conversation.objects.get(pk=conversation_id)
    serializer = CoversationDetailSerializer(converation)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def create_get_conversation(request, user_id):
    user = User.objects.get(pk=user_id)
    
    conversation = Conversation.objects.filter(users__in=list([request.user])).filter(users__in=list([user]))
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.users.add(request.user, user)
        conversation.save()
    
    return JsonResponse(data=True, safe=False)


@api_view(['POST'])
def send_message(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    
    for user in conversation.users.all():
        if user != request.user:
            receiver = user

    message = ConversationMessage.objects.create(
        conversation=conversation,
        created_by=request.user,
        received_by=receiver,
        body=request.data.get('body'),
    )
    
    conversation.modified_at = timezone.now()
    conversation.save()
    
    serializer = ConversationMessageSerializer(message)
    return JsonResponse({
        'message': serializer.data,
        'modified': conversation.modified_at_formatted(),
        }, safe=False)