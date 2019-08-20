from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class LoginManager(models.Manager):
    def validate_me(self, postData):
        errors={}
        if Users.objects.filter(email=postData['email']):
            errors['email'] = "The user exists, please log in."
        else:    
            if len(postData['first_name']) < 2:
                errors['first_name'] = "the first name cannot be blank."
            elif str.isalpha(postData['first_name'])==False and len(postData['first_name']) >1:
                errors['first_name'] = "the first name cannot contain numbers."
            if len(postData['last_name']) < 2:
                errors['last_name'] = "the last name cannot be blank."
            elif str.isalpha(postData['last_name'])==False and len(postData['last_name']) >1:
                errors['last_name'] = "the last name cannot contain numbers."
            if len(postData['email']) < 2:
                errors['email'] = "Email cannot be blank."
            elif not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Please try a different email address"
            if len(postData['password']) < 8 and len(postData['password']) >2:
                errors['password'] = "Password needs to be more than 7 characters."
            elif len(postData['password']) < 8:
                errors['password'] = "Your password cannot be blank."
            if len(postData['confirm_password']) < 8:
                errors['confirm_password'] = "Password confirmation cannot be blank."
            if postData['password'] != postData['confirm_password']:
                errors['password'] = "The passwords do not match"


        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager() # add this line!
