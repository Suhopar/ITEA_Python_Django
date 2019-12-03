from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.users.managers import CustomUserManager
from .tasks import send_mail_task


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128, blank=True)
    surname = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, unique=True, db_index=True)
    phone = models.CharField(max_length=12, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']


    class Meta:
        verbose_name = 'custom user'
        verbose_name_plural = 'custom users'

    @property
    def get_full_name(self):
        return '{} {}'.format(self.name.title(), self.surname.title())

    @property
    def get_short_name(self):
        return self.name

    def send_user_mail(self, subject, message):
        send_mail_task.delay(subject, message, self.email)
        # send_mail(subject, message, settings.EMAIL_HOST_USER, [self.email])
