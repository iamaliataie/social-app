from django.urls import path
from . import api

urlpatterns = [
    path(
        "",
        api.post_list,
        name="home"
    ),
    path(
        "<uuid:post_id>/",
        api.post_detail,
        name="post_detail"
    ),
    path(
        "post_create/",
        api.post_create,
        name="post_create"
    ),
    path(
        "<uuid:post_id>/comment_create/",
        api.comment_create,
        name="comment_create"
    ),
    path(
        "<uuid:post_id>/like_post/",
        api.like_post,
        name="like_post"
    ),
    path(
        "notifications/",
        api.notifications,
        name="notifications"
    ),
]
