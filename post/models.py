from django.db import models

from common.models import UserProfile


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    image = models.ImageField(upload_to='post')
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title
