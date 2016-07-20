from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title
