from __future__ import unicode_literals
from django.db import models
from apps.app_login.models import *
import re



class Actors(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Movies(models.Model):
    user = models.ForeignKey(Users,related_name="movies", on_delete=models.CASCADE)
    actors = models.ForeignKey(Actors,related_name="movies", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    user = models.ForeignKey(Users,related_name="reviews", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,related_name="reviews", on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)