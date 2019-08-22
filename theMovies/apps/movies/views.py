from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages
import bcrypt
    
def movies(request):
  
    try:
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        context = {
        'review' : Reviews.objects.all(),
        'users_info' : Users.objects.all(), 
        'reviews' : Movies.objects.all(),

        }
        print(context['reviews'][0].title)
        return render(request, 'movies/index.html', context)
    
    except:
        return render(request, 'app_login/denied.html')




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





def user_detail(request):
    try:
        context = {
             "users" : request.session["id"]  
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
             "users" : request.session["id"]  
        }
        return render(request, 'movies/add_movie.html', context)
    except:
        return render(request, 'app_login/denied.html')    


def add_review(request):

    if request.method=="POST":
        user_id = int(request.session["id"])
        user_id = Users.objects.get(id=user_id)
        movies_id = request.POST['movies_id']
        Reviews.objects.create(user=user_id, movie={movies_id}, review=request.POST['review'], rating=request.POST['rating'])
        
        
        return redirect(f'/movies/{movies_id}')


def delete_review(request):
    try:
        context = {
             "users" : request.session["id"]  
        }
        return render(request, 'movies/index.html', context)
    except:
        return render(request, 'app_login/denied.html')


# def wall(request):
#     try:
#         user_id = int(request.session["id"])
#         user_id = Users.objects.get(id=user_id)
#         context = {
#              "user" : user_id,
#              "message_scroll": Messages.objects.all(),
#              "comment_scroll": Comments.objects.all()
#         }
#         return render(request, 'app_wall/index.html', context)
#     except:
#         return render(request, 'app_login/denied.html')

# def add_movies(request):
#     try:
#         context = {
#              "users" : request.session["id"]  
#         }
#         return render(request, 'movies/index.html', context)
#     except:
#         return render(request, 'app_login/denied.html')

# def movie_page(request):
#     try:
#         context = {
#              "users" : request.session["id"]  
#         }
#         return render(request, 'movies/index.html', context)
#     except:
#         return render(request, 'app_login/denied.html')


# def user_page(request):
#     try:
#         context = {
#              "users" : request.session["id"]  
#         }
#         return render(request, 'movies/index.html', context)
#     except:
#         return render(request, 'app_login/denied.html')




#POST TO WALL FUNCTION
# def movies_post( request):
#     user_id = int(request.session["id"])
#     user_id = Users.objects.get(id=user_id)
#     Messages.objects.create(user=user_id, message=request.POST['message'])
#     return redirect("/movies")



#MESSAGES SCROLL
# def message_scroll(request): 
#     context = {
#     	"message_scroll": Messages.objects.all(),
        
#     }
#     return render(request, "app_wall/index.html", context)


#COMMENTS TO WALL FUNCTION
# def comment_post( request):
#     user_id = int(request.session["id"])
#     user_id = Users.objects.get(id=user_id)
#     message_id = int(request.POST["message_id"])
#     message_id = Messages.objects.get(id=message_id)
#     Comments.objects.create(user=user_id, message=message_id, comment=request.POST['comment'])
#     return redirect("/wall")


#COMMENTS SCROLL
# def comments_scroll(request): 
#     context = {
#     	"comment_scroll": Comments.objects.all(),
        
#     }
#     return render(request, "app_wall/index.html", context)


#DELETE COMMENTS
# def comments_delete( request, comments_id):

#     Comments.objects.get(id = comments_id).delete()
#     return redirect("/wall")


# def shows_new(request): 
  
#     return render(request, "shows/index.html")




# def checkout(request): #FUNCTION FOR THE CHECKOUT ON THE SHOW ALL MODAL
#     quantity_from_form = int(request.POST["quantity"])
#     item = int(request.POST["hidden"])
#     price_from_form = Store.objects.get(id=item)
#     total_charge = quantity_from_form * price_from_form.price
#     print("Charging credit card...")
#     Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
#     return redirect("/receipt")

# def receipt(request): #LANDING PAGE FOR THE CHECKOUT FUNCTION
#     total_amount = 0
#     for x in Order.objects.all():
#         total_amount += x.total_price

#     context = {
#     	'orders': Order.objects.last(),
#         'total': total_amount
#     }

#     return render(request, "shows/receipt.html", context)


# def shows_edit(request, shows_id): 
#     print ("I am before the if")
#     context = {
#         'shows' : Shows.objects.get(id = shows_id),
#         'all_shows' : Shows.objects.all(),
#     }
#     return render(request, "shows/edit.html", context)

# def shows_edit_me( request, shows_id):
#     errors = Shows.objects.basic_validator(request.POST)
#         # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect(f"shows/{shows_id}/edit.html")
#     else:
#         Shows.objects.filter(id=request.POST['id']).update(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], description=request.POST['description'])
#     return redirect("/shows")




# def shows_view(request, shows_id): 
#     context = {
        
#         'shows' : Shows.objects.get(id = shows_id),
#         'all_shows' : Shows.objects.all(),
#         'store' : Shows.objects.get(id = shows_id),
#     }
#     return render(request, "shows/show_detail.html", context)



# def shows_newbie(request):

#     Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], description=request.POST['description']) 
#     return redirect("/shows")

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