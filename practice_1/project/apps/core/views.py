from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm
from apps.users.models import CustomUser


def index_view(request):
    ctx = {}
    ctx['post_list'] = Post.objects.all()
    return render(request, 'core/index.html', ctx)


def post_view(request, pk, slug):
    ctx = {}
    # form_class = CommentForm
    # success_url = reverse_lazy('core:index')

    post = Post.objects.filter(pk=pk).first()
    comment_list = Comment.objects.filter(post=post).all()
    user = CustomUser.objects.filter(phone=request.user).first()
    # Comment(author=user, text_comment=text, post=post).save()
    if request.method == 'POST':
        text = request.POST.get('text_comment')
        Comment(author=user, text_comment=text, post=post).save()
        print('>>>', text, user)

    if post:
        ctx['user'] = user
        ctx['post'] = post
        ctx['comment_list'] = comment_list
    return render(request, 'core/post.html', ctx)


class CreatePostView(FormView):
    template_name = 'core/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        user = CustomUser.objects.filter(phone=self.request.user).first()
        title = self.request.POST.get('title')
        description = self.request.POST.get('description')
        text = self.request.POST.get('text')
        image = self.request.POST.get('image')
        Post(author=user, title=title, description=description, text=text, image=image).save()
        return super().form_valid(form)
