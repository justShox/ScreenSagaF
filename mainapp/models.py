from django.db import models
from django.forms import FileInput
from django.contrib.auth.models import User


# Create your models here.


# Категории для фильмов
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# База с фильмами
class Movie(models.Model):
    name = models.CharField(max_length=128)
    city = models.TextField(max_length=128)
    description = models.TextField(max_length=1024)
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    movie_image = models.ImageField(upload_to='static/image/')
    movie_video = models.FileField(upload_to='static/media', default='')
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# База с пользователями
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

