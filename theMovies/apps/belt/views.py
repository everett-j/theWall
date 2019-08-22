from django.shortcuts import render, redirect, reverse
from apps.app_login.models import *
from apps.app_wall.models import *
from apps.movies.models import *
from django.contrib import messages
import bcrypt

#BELT EXAM VIEWS

def belt(request):
  
    try:
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        context = {
        "user" : user_id,
        'review' : Reviews.objects.all(),
        'users_info' : Users.objects.all(), 
        'reviews' : Movies.objects.all(),

    }

        return render(request, 'belt/index.html', context)
    except:
        return render(request, 'app_login/denied.html')
   