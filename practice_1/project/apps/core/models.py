from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.urls import reverse

from apps.users.models import CustomUser


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='title',
        max_length=255,
        unique=True
    )
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        null=True
    )
    description = models.TextField(
        verbose_name='description',
        max_length=255,
        blank=True
    )
    text = models.TextField(
        verbose_name='text',
        max_length=1024
    )
    image = models.ImageField(
        verbose_name='image',
        upload_to='post',
        null=True,
        blank=True
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name='дата последнего изменения',
        auto_now=True
    )

    @property
    def short_description(self):
        return self.description[:20] + '...' if len(self.description) > 20 else self.description

    def get_absolute_url(self):
        return reverse('core:post', kwargs={'slug': self.slug, 'pk': self.pk})

    @property
    def get_count_comment_for_post(self):
        return len(Comment.objects.filter(post=(Post.objects.filter(pk=self.pk).first())).all())



class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        verbose_name='post',
        on_delete=models.CASCADE
    )
    text_comment = models.TextField(
        verbose_name='text comment',
        max_length=255,
        blank=True
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        default=timezone.now
    )