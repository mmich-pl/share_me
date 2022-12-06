from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Post(models.Model):
    captions = models.CharField(max_length=255)
    video = models.FileField(upload_to="video/%y")
    likes = models.ManyToManyField(User, related_name='video_like', blank=True)
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        unique_together = ["captions", "topic"]

    def __str__(self):
        return self.captions


class Comment(models.Model):
    content = models.CharField(max_length=255)
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    postedAt = models.DateField(default=datetime.today)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.content
