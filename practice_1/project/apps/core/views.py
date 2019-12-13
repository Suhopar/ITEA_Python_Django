from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, RedirectView, ListView, DetailView, View, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment, Category, Like, News
from .forms import PostForm
from apps.users.models import CustomUser


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()

        return context


class NewsView(TemplateView):
    template_name = 'core/news.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all()

        return context


class PostDetailView(DetailView):
    template_name = 'core/post.html'
    model = Post

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comment_list = Comment.objects.filter(post=post).all()
        user = get_user_model().objects.filter(phone=self.request.user.phone).first()
        post_like = Like.objects.filter(user=user, post=post).first()
        print(post.pub_date)

        if post:
            context['post'] = post
            context['comment_list'] = comment_list
            # print(request.user.email)
        if not post_like:
            context['like_user'] = True
            context['like_text'] = 'Like'
        else:
            context['like_text'] = 'Dislike'
        return context


class AddCommentView(View):

    def post(self, request, *args, **kwargs):
        comment = Comment(request)
        pk = self.kwargs.get('pk')
        text = self.request.POST.get('text_comment')
        post = Post.objects.filter(pk=pk).first()
        user = self.request.user
        Comment(author=user, text_comment=text, post=post).save()
        return redirect(str(post.get_absolute_url()))


class LikePostView(View):

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        user = self.request.user
        post_like = Like.objects.filter(user=user, post=post).first()
        if not post_like:
            Like(user=user, post=post).save()
        else:
            post_like.delete()
        return redirect(str(post.get_absolute_url()))


class RemovePostView(View):

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        user = self.request.user
        if post.author == user:
            post.delete()
        return redirect('users:profile')


class RemoveCommentView(View):

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comment = Comment.objects.filter(pk=pk).first()
        post = comment.post
        user = self.request.user
        if comment.author == user:
            comment.delete()
        return redirect(post.get_absolute_url())


class CreatePostView(FormView):
    template_name = 'core/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('core:index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        user = get_user_model().objects.filter(phone=self.request.user.phone).first()
        category = Category.objects.filter(title=self.request.POST.get('category')).first()
        post = form.save(commit=False)
        post.author = user
        post.category = category
        # print(dir(post))
        post.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class CategoryListView(ListView):
    template_name = 'core/category_list.html'
    queryset = Category.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_list = list()
        for category in Category.objects.all():
            # print('>>>', category.post_set)
            category_list.append({
                'url': category.get_absolute_url(),
                'title': category.title.title(),
                'count': category.post_set.count()
            })
        context['category_list'] = category_list
        return context


class CategoryDetailView(DetailView):
    template_name = 'core/category.html'
    model = Category

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        context['product_list'] = category.post_set.all()
        return context


class TopFivePostListView(ListView):
    template_name = 'core/top_five_post_list.html'
    queryset = Post.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_list = list()
        post_list = list()
        for post in Post.objects.all()[:5]:
            print(post.get_count_like)
            count_list.append((post.get_count_like, post.pk))

        for i, e in sorted(count_list, reverse=True):
            post_list.append(Post.objects.filter(pk=e).first())

        context['post_list'] = post_list
        return context

# class EditPostFormView(FormView):
#     template_name = 'core/edit_post.html'
#     form_class = PostForm
#     success_url = reverse_lazy('core:profile')
#     post = Post
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Post, pk=pk)
#
#     def get_context_data(self, **kwargs):
#         print('>>>ok', self.kwargs.get('pk'))
#         context = super().get_context_data(**kwargs)
#         # pk = self.post
#         context['post'] = self.post
#         context['category_list'] = Category.objects.all()
#         return context
#
#     def form_valid(self, form):
#         user = get_user_model().objects.filter(phone=self.request.user.phone).first()
#         category = Category.objects.filter(title=self.request.POST.get('category')).first()
#         post = form.save(commit=False)
#         post.author = user
#         post.category = category
#         # print(dir(post))
#         post.save()
#         return super().form_valid(form)


#
# class UpdatePostView(UpdateView):
#     template_name = 'core/create_post.html'
#     form_class = PostForm
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Post, pk=pk)
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
