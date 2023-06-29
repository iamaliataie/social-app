from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_conversations, name='get_conversations'),
    path('<uuid:conversation_id>/', api.get_active_conversation, name='get_active_conversations'),
    path('<uuid:conversation_id>/send_message/', api.send_message, name='send_message'),
    path('create_get_conversation/<uuid:user_id>/', api.create_get_conversation, name='create_get_conversation')
]