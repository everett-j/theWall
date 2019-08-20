from __future__ import unicode_literals
from django.db import models
from apps.app_login.models import *
import re



class Messages(models.Model):
    user = models.ManyToManyField(Users, related_name="Messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
