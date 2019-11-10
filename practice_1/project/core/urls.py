from django.urls import path, re_path
from .views import (
    index_view,
    post_view,
)

app_name = 'core'

urlpatterns = [
    path('', index_view, name='index'),
    path('posts/<slug>/<pk>/', post_view, name='post'),
]
