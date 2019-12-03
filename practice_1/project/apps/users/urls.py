from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import (
    ProfileView,
    LoginView,
    LogoutView,
    RegisterView
)


app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='users/pw_reset.html',
        success_url='/users/reset/done/'
    ), name='pw_reset'),
    path('reset/done/', TemplateView.as_view(template_name='users/pw_reset_done.html'), name='pw_reset_done'),
]
