from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=250)
    author = models.TextField()
    created_date = models.DateTimeField('date created')
    published_date = models.DateTimeField('date published')
    


class Author(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )