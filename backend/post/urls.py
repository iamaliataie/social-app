from django.urls import path
from . import api

urlpatterns = [
    path(
        "",
        api.home,
        name=""
    ),
]
