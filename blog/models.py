from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)

    def __str__(self):
        return self.username


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey('blog.User', on_delete=models.CASCADE, null=True, related_name='comments')
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name='comments')
    comment = models.TextField(max_length=150, blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    author = models.ForeignKey('blog.User', on_delete=models.CASCADE, limit_choices_to={'is_staff': True},
                               related_name='posts')
    title = models.CharField(max_length=50, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=1000, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(upload_to='blog/images/', null=True, blank=True)

    def __str__(self):
        return self.title
