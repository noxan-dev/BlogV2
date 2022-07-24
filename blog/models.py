from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)

    def __str__(self):
        return self.username


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=150, blank=True, )

    def __str__(self):
        return self.comment


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True},
                               related_name='posts')
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.title
