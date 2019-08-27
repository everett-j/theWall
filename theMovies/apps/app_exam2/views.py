from django.shortcuts import render, redirect, reverse
from apps.app_login.models import *
from apps.app_wall.models import *
from apps.movies.models import *
from apps.belt.models import *
from apps.app_two.models import *
from apps.app_exam2.models import *
from django.contrib import messages
import bcrypt

#EXAM 2 BACKUP VIEWS


##HOME PAGE ##SORTED BY CREATED DATE
def index(request):
  
    try:
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        context = {
        "user" : user_id,
        'review' : Reviews.objects.all(),
        'users_info' : Users.objects.all(), 
        'trips' : Trips.objects.order_by("-created_at"),

    }

        return render(request, 'app_two/index.html', context)
    except:
        return render(request, 'app_login/denied.html')