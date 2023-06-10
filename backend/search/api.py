from django.http import JsonResponse
from rest_framework.decorators import api_view
from account.models import User
from account.serializers import UserSerializer
from post.models import Post
from post.serializers import PostSerializer

@api_view(['POST'])
def search(request):
    
    form = request.data
    users = User.objects.filter(name__icontains=form['query'])
    users_serializer = UserSerializer(users, many=True)
    posts = Post.objects.filter(body__icontains=form['query'])
    posts_serializer = PostSerializer(posts, many=True)
    context = {
        'users': users_serializer.data,
        'posts': posts_serializer.data
    }
    return JsonResponse(context, safe=False)