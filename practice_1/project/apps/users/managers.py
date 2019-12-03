from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.db.models import QuerySet, Manager


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, phone, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        user = self.model(email=email, phone=phone,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone, password=None, **extra_fields):
        return self._create_user(email, phone, password, False, False,
                                 **extra_fields)

    def create_superuser(self, phone, email, password, **extra_fields):
        return self._create_user(email, phone, password, True, True,
                                 **extra_fields)