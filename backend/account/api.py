from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer
from .forms import SignupForm, EditProfileForm
from post.models import Post, Notification
from post.serializers import PostSerializer

@api_view(['GET'])
def authenticated_user(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'avatar': request.user.get_avatar(),
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


@api_view(['POST'])
def edit_profile(request):
    
    form = EditProfileForm(request.POST, request.FILES, instance=request.user)
    status = False
    message = 'Something went wrong. Please try again!'
    if form.is_valid():
        form.save()
        status = True
        message = 'Your information updated successfully!'
    else: print('failed')
    return JsonResponse({
        'status': status, 
        'message': message, 
        'info': { 
            'name': request.user.name,
            'email': request.user.email,
            'avatar': request.user.get_avatar()
            }
        })


@api_view(['POST'])
def password_change(request):
    
    form = PasswordChangeForm(request.user, request.POST)
    message = None
    status = False
    if form.is_valid():
        message = 'Password changed successfully.'
        status = True
        form.save()
    else:
        message = form.errors.as_json()
    
    return JsonResponse({'status': status, 'message': message})


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
    Notification.objects.create(
        body=f'{request.user.name} sent you a friendship request.',
        request=friendship,
        created_by=request.user,
        created_for=friendship.received_by,
    )
    
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
            Notification.objects.create(
                body=f'{friendship_request.received_by} accepted your friendship request.',
                created_by=friendship_request.received_by,
                created_for=friendship_request.created_by,
            )
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


@api_view(['GET'])
def friend_suggesstions(request):
    suggesstion_list = list()
    for friend in request.user.friends.all():
        for f in friend.friends.all():
            if f != request.user and f not in request.user.friends.all() and f not in suggesstion_list:
                suggesstion_list.append(f)
    serializer = UserSerializer(suggesstion_list, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    user_exists = User.objects.filter(email=data['email']).first()
    message = None
    status = False
    form = SignupForm({
        'name': data.get('name'),
        'email': data.get('email'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        message = 'User registered successfully'
        status = True
    else:
        message = form.errors.as_json()
        status = False
        
    return JsonResponse({'status': status, 'message': message})


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def activate_account(request, user_id, user_email):
    print('acctivation method')
    user = User.objects.filter(pk=user_id, email=user_email).first()
    if user:
        user.is_active = True
        user.save()
        return HttpResponse('<h1>Account activated succssfully. Thank You!</h1>')
    else:
        return JsonResponse({'message': 'user not found'})