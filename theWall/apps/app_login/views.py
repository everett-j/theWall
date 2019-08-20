from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

        #LOGIN and REGISTER

def validate_login(request):
    users = Users.objects.get(email=request.POST['email']) 
    if bcrypt.checkpw(request.POST['password'].encode(), users.pw_hash.encode()):
        print("password match")
    else:
        print("failed password")


def register(request):    
    request.session.clear()
    errors = Users.objects.validate_me(request.POST)
    
    if len(errors):
        for key,value in errors.items():
            messages.error(request,value, extra_tags="register_error:"+str(key))
        return redirect("/login")

    else:
        users = Users.objects.create()
        users.first_name = request.POST['first_name']
        users.last_name= request.POST['last_name']
        users.email = request.POST['email']
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        users.password = hash1
        
        users.save()
        request.session['users'] = users.first_name
        request.session['id']= users.id
        messages.success(request, "User successfully added.")
        return redirect("/success")

def login(request):
    request.session.clear()
    if len(request.POST['email']) < 1:
        messages.error(request, "Email cannot be blank.")
    if len(request.POST['password']) < 1:
        messages.error(request,"Password cannot be blank")
    if len(request.POST['email']) > 1 and len(request.POST['password']) > 0:
        print (request.POST['email'])
        if len(Users.objects.filter(email=request.POST['email'])) > 0:
            user = Users.objects.get(email=request.POST['email'])
            print (user)
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user'] = user.first_name
                request.session['id'] = user.id
                return redirect("/success")
            else:
                messages.error(request,'Wrong Password')
                return redirect("/login")
        else:
            messages.error(request,'User does not exist, please register')
            return redirect("/login")
    return redirect("/success")



def success(request): 
    try:
        context = {
             "users" : request.session["id"]  
        }
        return render(request, 'app_login/success.html', context)
    except:
        return render(request, 'app_login/denied.html')
        
    
   


def logout(request): 
    request.session.clear()
    return redirect("/login")




def denied(request): 
  
    return redirect( "app_login/denied.html")





def loginregister(request): 
  
    return render(request, "app_login/registration.html")

