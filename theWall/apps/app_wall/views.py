from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
    
def index(request):
  
    return render(request, 'app_wall/index.html')


# def shows_new(request): 
  
#     return render(request, "shows/index.html")


# def shows_all(request): #FUNCTION FOR THR SHOW ALL PAGE
#     context = {
#     	"shows_all": Shows.objects.all(),
#         'store' : Store.objects.all(),
#     }
#     return render(request, "shows/shows.html", context)

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



# def shows_delete( request, shows_id):
#     Shows.objects.get(id = shows_id).delete()
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