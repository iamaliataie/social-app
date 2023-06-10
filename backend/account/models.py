import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError('You have not provided a valid email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    # avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    friends = models.ManyToManyField('self', blank=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return self.name
     
    def friends_count(self):
        return self.friends.count()
    

class FriendshipRequest(models.Model):
    SENT = 'sent'
    ACCEPT = 'accepted'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_made')
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_received')
    created_at = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return f'{ self.created_by.name } to { self.received_by.name }'
    
    def created_at_formatted(self):
        return timesince.timesince(self.created_at)