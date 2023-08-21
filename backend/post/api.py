from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Post, Comment, Notification
from .serializers import PostSerializer, CommentSerializer,NotificationSerializer


@api_view(['GET'])
def post_list(request):
    ids = [request.user.id]
    for friend in request.user.friends.all():
        ids.append(friend.id)
    
    posts = Post.objects.filter(created_by__in=list(ids))
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_create(request):
    form = request.data
    new_post = Post.objects.create(
        body=form['body'],
        image=form['image'],
        created_by=request.user
    )
    if new_post:
        serializer = PostSerializer(new_post)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'status': False})


@api_view(['GET'])
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def comment_create(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.create(
        body=request.data['body'],
        created_by=request.user
    )
    
    if comment:
        post.comments.add(comment)
        post.save()
        if request.user is not post.created_by:
            Notification.objects.create(
            body=f'{request.user.name} commented on your post {post.body[:10]}',
            post=post,
            created_by=request.user,
            created_for=post.created_by,
        )
        
    serializer = CommentSerializer(comment)    
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.user not in post.likes.all():
        post.likes.add(request.user)
        post.save()
        if request.user is not post.created_by:
            Notification.objects.create(
            body=f'{request.user.name} liked your post {post.body[:10]}',
            post=post,
            created_by=request.user,
            created_for=post.created_by,
        )
    else:
        post.likes.remove(request.user)
        post.save()
    
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def notifications(request):
    notifications = Notification.objects.filter(created_for=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return JsonResponse(serializer.data, safe=False)
