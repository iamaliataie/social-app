from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer
from .forms import SignupForm
from post.models import Post
from post.serializers import PostSerializer

@api_view(['GET'])
def authenticated_user(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['GET'])
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user_serializer = UserSerializer(user)
    
    posts = Post.objects.filter(created_by=user)
    posts_serializer = PostSerializer(posts, many=True)
    
    friendship = 0
    if user is not request.user:
        if user in request.user.friends.all():
            friendship = 3
        elif FriendshipRequest.objects.filter(created_by=user, received_by=request.user).exists():
            friendship = 2
        else:
            if FriendshipRequest.objects.filter(created_by=request.user, received_by=user).exists():
                friendship = 1
    
    context = {
        'user': user_serializer.data,
        'posts': posts_serializer.data,
        'friendship': friendship
    }
    return JsonResponse(context, safe=False)


@api_view(['GET'])
def friends(request, user_id):
    user = User.objects.get(pk=user_id)
    friends = user.friends.all()
    requests = FriendshipRequest.objects.filter(received_by=user)
    friends_serializer = UserSerializer(friends, many=True)
    requests_serializer = FriendshipRequestSerializer(requests, many=True)
    
    context ={
        'friends': friends_serializer.data,
        'requests': requests_serializer.data,
    }
    return JsonResponse(context, safe=False)


@api_view(['POST'])
def friendship_create(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    friendship = FriendshipRequest.objects.create(created_by=request.user, received_by=user)
    serializer = FriendshipRequestSerializer(friendship)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def friendship_handle(request, user_id, status):
    user = User.objects.filter(pk=user_id).first()
    friendship_request = FriendshipRequest.objects.filter(created_by=user, received_by=request.user).first()
    friendship = 1
    if friendship_request:
        if status == 'accept':
            request.user.friends.add(user)
            friendship_request.delete()
            friendship = 3
        else:
            friendship_request.delete()
            friendship = 0
    else:
        if status == 'remove':
            request.user.friends.remove(user)
        elif status == 'cancel':
            friendship_request = FriendshipRequest.objects.filter(created_by=request.user, received_by=user).first()
            friendship_request.delete()
        friendship = 0
    
    friends = request.user.friends.all()
    requests = FriendshipRequest.objects.filter(received_by=request.user)
    friends_serializer = UserSerializer(friends, many=True)
    requests_serializer = FriendshipRequestSerializer(requests, many=True)
    
    return JsonResponse({
        'friendship': friendship,
        'friends': friends_serializer.data,
        'requests': requests_serializer.data,
        }, safe=False)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    user_exists = User.objects.filter(email=data['email']).first()
    message = ''
    status = False
    if not user_exists:
        form = SignupForm({
            'name': data.get('name'),
            'email': data.get('email'),
            'password1': data.get('password1'),
            'password2': data.get('password2'),
        })
        
        if form.is_valid():
            form.save()
            message = 'User registered successfully'
            status = True
        else:
            print(form.errors)
            message = 'Registration failed. Try again'
            status = False
    else:
        message = 'User with this email already exists'
        status = False
        
    return JsonResponse({'status': status, 'message': message})

