from django.urls import path, re_path
from .views import (
    index_view,
    post_view,
    CreatePostView,
)

app_name = 'core'

urlpatterns = [
    path('', index_view, name='index'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('posts/<slug>/<pk>/', post_view, name='post'),
]
