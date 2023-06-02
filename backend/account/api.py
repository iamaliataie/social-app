from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User
from .forms import SignupForm

@api_view(['GET'])
def authenticated_user(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })
    
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