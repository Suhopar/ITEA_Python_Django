from django.urls import path, re_path
from .views import (
    IndexView,
    # post_view,
    PostDetailView,
    CreatePostView,
    CategoryListView,
    CategoryDetailView,
    AddCommentView,
    LikePostView,
    RemovePostView,
    RemoveCommentView,
    TopFivePostListView,
    NewsView,
    # EditPostView,
    # EditPostFormView,
    # UpdatePostView,
)

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug>/', CategoryDetailView.as_view(), name='category'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    # path('posts/<slug>/<pk>/update', UpdatePostView.as_view(), name='post-update'),

    path('posts/<slug>/<pk>/', PostDetailView.as_view(), name='post'),
    path('like_post/<pk>/', LikePostView.as_view(), name='like-post'),
    path('add_comment/<pk>/', AddCommentView.as_view(), name='add-comment'),
    path('remove_post/<pk>/', RemovePostView.as_view(), name='remove-post'),
    path('remove_comment/<pk>/', RemoveCommentView.as_view(), name='remove-comment'),
    path('top_five_post_list/', TopFivePostListView.as_view(), name='top_five_post_list'),
    path('news/', NewsView.as_view(), name='news'),

    # path('edit_post/<pk>/', EditPostView.as_view(), name='edit-post'),
    # path('edit_post/<pk>/', EditPostFormView.as_view(), name='edit_post'),
]
