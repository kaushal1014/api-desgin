
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateField(auto_now_add=True)
    first_name=models.CharField(max_length=100)

    def __str__(self):
        return f"The title is {self.title}"
