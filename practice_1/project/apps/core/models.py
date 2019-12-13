from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.urls import reverse
from apps.users.models import CustomUser


class Category(models.Model):
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = None
        super().save(*args, **kwargs)


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
    category = models.ForeignKey(
        Category,
        verbose_name='category',
        on_delete=models.CASCADE,
        null=True
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
        max_length=2048
    )
    image = models.ImageField(
        verbose_name='image',
        upload_to='post',
        null=True,
        blank=True
    )
    pub_date = models.DateTimeField(
        verbose_name='publication date',
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name='last modified date',
        auto_now=True
    )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'

    def __str__(self):
        return 'title: {} '.format(self.title)

    @property
    def short_description(self):
        return self.description[:20] + '...' if len(self.description) > 20 else self.description

    def get_absolute_url(self):
        return reverse('core:post', kwargs={'slug': self.slug, 'pk': self.pk})

    @property
    def get_count_comment_for_post(self):
        return len(Comment.objects.filter(post=(Post.objects.filter(pk=self.pk).first())).all())

    @property
    def get_count_like(self):
        return len(Like.objects.filter(post=(Post.objects.filter(pk=self.pk).first())).all())


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser,
        verbose_name='author',
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
        verbose_name='publication date',
        default=timezone.now
    )


class Like(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='user',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        verbose_name='post',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.slug = None
        super().save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=255,
        unique=True
    )
    text = models.TextField(
        verbose_name='text',
        max_length=255,
        blank=True
    )
    pub_date = models.DateTimeField(
        verbose_name='publication date',
        default=timezone.now
    )