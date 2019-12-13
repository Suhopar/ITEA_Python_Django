from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.core.models import Post

from .serializers import PostSerializer


# class PostAPIView(APIView):
class PostAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('title',)
    search_fields = ('title',)
    ordering_fields = ('title', 'description')

    #
    #     def get(self, request):
    #         post_qs = Post.objects.all()
    #         serializer = PostSerializer(post_qs, many=True)
    #         return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'ok', 'product': serializer.data})

    def put(self, request, pk):
        product = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'ok'})

    def delete(self, request, pk):
        product = get_object_or_404(Post, pk=pk)
        product.delete()
        return Response({'status': 'ok'})
