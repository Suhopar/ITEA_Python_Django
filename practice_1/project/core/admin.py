from django.contrib import admin
from .models import Post, Comment


# @admin.register(Post)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'discount')
#     list_display_links = ('title', )


admin.site.register(Post)
admin.site.register(Comment)

