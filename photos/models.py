from django.db import models
from django.conf import settings


# Create your models here.
class Photo(models.Model):

    title = models.CharField(max_length=100)
    photo = models.ImageField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='votes')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):

    content = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username
