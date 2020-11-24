from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])