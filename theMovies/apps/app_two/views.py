from django.shortcuts import render, redirect, reverse
from apps.app_login.models import *
from apps.app_wall.models import *
from apps.movies.models import *
from apps.belt.models import *
from apps.app_two.models import *
from django.contrib import messages
import bcrypt

#EXAM 2 VIEWS - TUESDAY

def redirect_home(request):
                       
        return redirect('/trips/dashboard')



##HOME PAGE ##SORTED BY CREATED DATE
def belt(request):
  
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


### CANCEL BUTTON FUNCTION
def cancel_redirect(request):
                       
        return redirect('/trips/dashboard')


####### WITH VALIDATION  ADD NEW TRIP #########
def new_trip( request):
    errors = Trips.objects.validate_me(request.POST)
    if len(errors):
        for key,value in errors.items():
            messages.error(request,value, extra_tags="register_error:"+str(key))
        return redirect("/trips/new")
    else:
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        Trips.objects.create(user=user_id, destination=request.POST['destination'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], plan=request.POST['plan'])
        
        messages.success(request, "Trip successfully added.")
    return redirect("/trips/dashboard")




#VIEW FUNCTION OF EDIT TRIP
def edit_trip(request, t_id):

    user_id = int(request.session["id"])
    user_id = Users.objects.get(id=user_id)
    try:
        context = {
            "user" : user_id,
        "users_id" : request.session["id"],
        't_id' : Trips.objects.get(id = t_id),
    
        'trips' : Trips.objects.filter(id = t_id)
        }
        return render(request, 'app_two/edit_trip.html', context)
    except:
        return render(request, 'app_login/denied.html')


#DELETE A TRIP FUNCTION
def trips_delete( request, trips_id):
    Trips.objects.get(id = trips_id).delete()
    return redirect("/trips/dashboard")

#POST FUNCTION OF EDIT TRIP
#USES A FILTER FOR TRIP ID TO UPDATE ONLY THAT TRIP
def update_redirect( request):
    trip_id = int(request.POST['trip_id'])
    Trips.objects.filter(id=trip_id).update(destination=request.POST['destination'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], plan=request.POST['plan'])
    return redirect("/trips/dashboard")




#FUNCTION FOR DETAILS OF TRIP
def detail_trip(request, t_id):
    user_id = int(request.session["id"])
    user_id = Users.objects.get(id=user_id)
    try:
        context = {
        "user" : user_id,
        "users_id" : request.session["id"],
        't_id' : Trips.objects.get(id = t_id),

        'trips' : Trips.objects.all()
        }
        return render(request, 'app_two//detail_trip.html', context)
    except:
        return render(request, 'app_login/denied.html')


#FUNCTION to RENDER NEW TRIP PAGE
def add_trip(request):
    try:
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        context = {
             
        "user" : user_id,
        'review' : Reviews.objects.all(),
        'users_info' : Users.objects.all(), 
        'reviews' : Movies.objects.all(),
        }
        return render(request, 'app_two/new_trip.html', context)
    except:
        return render(request, 'app_login/denied.html')
