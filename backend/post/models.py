import uuid
from django.db import models
from account.models import User

from django.utils import timezone, timesince

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/' ,null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True)
    comments = models.ManyToManyField('Comment', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return f'{self.created_by.name} - {self.body[:30]}'
    
    def created_at_formatted(self):
        return timesince.timesince(self.created_at)
    
    def get_image(self):
        if self.image:
            return f'http://127.0.0.1:8000{self.image.url}'
        else: return ''
    
class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    
    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return  '{} - {}'.format(self.created_by.name,self.body[:30])
    
    def created_at_formatted(self):
        return timesince.timesince(self.created_at)