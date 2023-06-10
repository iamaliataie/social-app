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
    path(
        'profile/<uuid:user_id>/',
        api.profile,
        name='profile'
    ),
    path(
        'profile/<uuid:user_id>/friends/',
        api.friends,
        name='friends'
    ),
    path(
        'friendship_create/<uuid:user_id>/',
        api.friendship_create,
        name='friendship_create'
    ),
    path(
        'friendship_handle/<uuid:user_id>/<str:status>/',
        api.friendship_handle,
        name='friendship_handle'
    ),
]