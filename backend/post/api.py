from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_create(request):
    form = request.data
    new_post = Post.objects.create(
        body=form['body'],
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
        
    serializer = CommentSerializer(comment)    
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.user not in post.likes.all():
        post.likes.add(request.user)
        post.save()
    else:
        post.likes.remove(request.user)
        post.save()
    
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data, safe=False)