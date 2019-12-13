from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('phone', 'is_active', 'is_superuser')
#     search_fields = ('phone',)
#     readonly_fields = ('date_joined',)
#     ordering = ('-date_joined',)
#     fieldsets = (
#         (None, {'fields': ('password',)}),
#         ('Personal info', {'fields': ('name', 'surname', 'phone',)}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('name', 'phone', 'password1', 'password2'),
#         }),
#      )
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'phone', 'is_active', 'is_superuser')
    search_fields = ('email', 'phone')
    readonly_fields = ('date_joined',)
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'phone', 'telegram_id')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'password1', 'password2'),
        }),
    )
