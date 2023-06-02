from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import api

urlpatterns = [
    path(
        'signup/',
        api.signup,
        name='signup'
    ),
    path(
        'login/',
        TokenObtainPairView.as_view(),
        name='login'
    ),
    path(
        'refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'authenticated_user/',
        api.authenticated_user,
        name='authenticated_user'
    ),
]