from django.contrib import admin
from .models import Post, Comment, Category, Like, News


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ('title', 'author')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'pub_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'pub_date')


@admin.register(News)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')

# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Category)
admin.site.register(Like)
