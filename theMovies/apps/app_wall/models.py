from __future__ import unicode_literals
from django.db import models
from apps.app_login.models import *
import re


class PostManager(models.Manager):
    def validate_messages(self, postData):
        errors={}

        if len(postData['message']) < 2:
            errors['message'] = "the message cannot be blank."
        elif str.isalpha(postData['message'])==False and len(postData['message']) >1:
            errors['message'] = "the first name cannot contain numbers."

        return errors

class CommentManager(models.Manager):
    def validate_comments(self, postData):
        errors={}

        if len(postData['comment']) < 2:
            errors['comment'] = "the message cannot be blank."


        return errors


class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager() # add this line!

class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.ForeignKey(Messages, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager() # add this line!