from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from uuid import uuid4
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)

    def __str__(self):
        return self.username


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey('blog.User', on_delete=models.CASCADE, null=True, related_name='comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name='comments')
    comment = RichTextField(max_length=150, config_name='comment-form', blank=False, null=True,
                            validators=[MaxLengthValidator(150, message=_('You have exceeded the amount of words')),
                                        MinLengthValidator(5)])

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    author = models.ForeignKey('blog.User', on_delete=models.CASCADE, limit_choices_to={'is_staff': True},
                               related_name='posts')
    title = models.CharField(max_length=50, blank=False, null=True)
    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(config_name='post-form', blank=False, null=True,
                         validators=[MaxLengthValidator(1000), MinLengthValidator(10)])
    posted_at = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(upload_to='blog/img/', null=True, blank=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title
