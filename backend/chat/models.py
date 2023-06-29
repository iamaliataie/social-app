import uuid
from django.db import models
from account.models import User
from django.utils import timezone, timesince

# Create your models here.

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    modified_at = models.DateTimeField(auto_now=timezone.now)
    
    def __str__(self) -> str:
        return ' - '.join([user.name for user in self.users.all()]) + self.modified_at_formatted()
    
    def created_at_formatted(self):
        return timesince.timesince(self.created_at)
    
    def modified_at_formatted(self):
        return timesince.timesince(self.modified_at)
    

class ConversationMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_by')
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_by')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    
    def __str__(self) -> str:
        return f'{self.created_by} to {self.received_by} - {self.created_at_formatted()}'
    
    def created_at_formatted(self):
        return timesince.timesince(self.created_at)