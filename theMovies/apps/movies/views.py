from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages
import bcrypt

#MOVIES APP ONLY

def movies(request):
  
    # try:
    user_id = int(request.session["id"])
    user_id = Users.objects.get(id=user_id)
    posts = Reviews.objects.all().order_by('-created_at')[:3]
    more_posts = Movies.objects.all().order_by('-created_at')[3:]
    context = {
    "user" : user_id,
    'review' : Reviews.objects.all(),
    'users_info' : Users.objects.all(), 
    'reviews' : Movies.objects.all(),
    'posts' : posts,
    'more_posts' : more_posts,
    }
    print(context['reviews'][0].title)
    return render(request, 'movies/index.html', context)
    
    # except:
    #     return render(request, 'app_login/denied.html')




def movie_detail(request, movies_id):
   
    try:
        context = {
                "users_id" : request.session["id"],
                'movies' : Movies.objects.get(id = movies_id),
        'actors' : Movies.objects.get(id = movies_id).actors,
        'users' : Users.objects.all(), 
        'reviews' : Movies.objects.get(id = movies_id).reviews.all()
        }
        return render(request, 'movies/movie_detail.html', context)
    except:
        return render(request, 'app_login/denied.html')





def user_detail(request, u_id):
    try:
        context = {
        "user_id" : request.session["id"],
        'user' : Users.objects.get(id = u_id),
        'movie' : Movies.objects.all()
        } 
        
        return render(request, 'movies/user_detail.html', context)
    except:
        return render(request, 'app_login/denied.html')


def add_redirect(request):
    print ("I am before the if")
    if request.method=="POST":
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        Actors.objects.create(name=request.POST['name'])
        actor_id = Actors.objects.filter(name=request.POST['name']).first()
        Movies.objects.create(user=user_id, actors=actor_id, title=request.POST['title'])
        thisMovie=Movies.objects.filter(title=request.POST['title']).first()
        Reviews.objects.create(user=user_id, movie=thisMovie, review=request.POST['review'], rating=request.POST['rating'])
        
        return redirect(f'/movies/{thisMovie.id}')
        


def add_movie(request):
    try:
        context = {
             "users" : request.session["id"],
             "actors" : Actors.objects.all()
        }
        return render(request, 'movies/add_movie.html', context)
    except:
        return render(request, 'app_login/denied.html')    


def add_review(request):

    if request.method=="POST":
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        movies_id = Movies.objects.get(id = request.POST['movies_id'])
        Reviews.objects.create(user=user_id, movie=movies_id, review=request.POST['review'], rating=request.POST['rating'])
        
        
        return redirect(f'/movies/{movies_id.id}')


def delete_review(request):
    try:
        context = {
             "users" : request.session["id"]  
        }
        return render(request, 'movies/index.html', context)
    except:
        return render(request, 'app_login/denied.html')

#EXTRA EXTRA - UPDATING DB - ROUTING TO SPECIFIC ID

def user_list(request):
  
    try:
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        posts = Reviews.objects.all().order_by('-created_at')[:3]
        more_posts = Movies.objects.all().order_by('-created_at')[3:]
        context = {
        "user" : user_id,
        'review' : Reviews.objects.all(),
        'users_info' : Users.objects.all(), 
        'reviews' : Movies.objects.all(),
        'posts' : posts,
        'more_posts' : more_posts,
        }
        print(context['reviews'][0].title)
        return render(request, 'movies/users.html', context)
    
    except:
        return render(request, 'app_login/denied.html')


def user_redirect(request):
        if request.method=="POST":
                user_id = int(request.session["id"])
                u_id = int(request.POST["id"])
                
                Users.objects.filter(id=u_id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
                
        return redirect('/movies/users')




def update_user(request, u_id):
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)

        try:
                context = {
                "user" : user_id,
                'users' : Users.objects.get(id = u_id),
                'review' : Reviews.objects.all(),
                'users_info' : Users.objects.all(), 
                'reviews' : Movies.objects.all(),
                
                }
                
                return render(request, 'movies/update_users.html', context)
        except:
                return render(request, 'app_login/denied.html')

#ADD NEW USER IN MODAL FUNCTION
def add_new_user(request):
        if request.method=="POST":
                Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
                
        return redirect('/movies/users')




# def update(request, id):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Shows.objects.basic_validator(request.POST)
#         # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#         return redirect("/shows")
#     else:
#         # if the errors object is empty, that means there were no errors!
#         # retrieve the blog to be updated, make the changes, and save
#         shows = Shows.objects.get(id = id)
#         shows.title = request.POST['title']
#         shows.description = request.POST['description']
#         shows.save()
#         messages.success(request, "Show successfully updated")
#         # redirect to a success route
#         return render(request, "shows/shows.html")