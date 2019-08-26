from __future__ import unicode_literals
from django.db import models
from apps.app_login.models import *

from apps.app_wall.models import *
import re


class FormManager(models.Manager):
    def validate_me(self, postData):
        errors={}

        if len(postData['destination']) < 2:
            errors['destination'] = "the destination cannot be blank."

        if len(postData['start_date']) < 2:
            errors['start_date'] = "the start date cannot be blank."

        if len(postData['end_date']) < 2:
            errors['end_date'] = "the end date cannot be blank."

        if len(postData['plan']) < 2:
            errors['plan'] = "the plan cannot be blank."

        return errors

class Trips(models.Model):
    user = models.ForeignKey(Users,related_name="trips", on_delete=models.CASCADE)
    destination = models.TextField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager() # add this line!



