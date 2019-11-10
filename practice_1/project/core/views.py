from django.shortcuts import render
from .models import Post, Comment


def index_view(request):
    ctx = {}
    ctx['post_list'] = Post.objects.all()
    return render(request, 'core/index.html', ctx)


def post_view(request, pk, slug):
    ctx = {}
    post = Post.objects.filter(pk=pk).first()
    comment_list = Comment.objects.filter(post=post).all()
    if post:
        ctx['post'] = post
        ctx['comment_list'] = comment_list
    return render(request, 'core/post.html', ctx)
