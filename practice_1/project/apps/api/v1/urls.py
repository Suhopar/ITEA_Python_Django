from django.urls import path
from .views import PostAPIView

urlpatterns = [

    path('post/', PostAPIView.as_view(), name='post'),
]
