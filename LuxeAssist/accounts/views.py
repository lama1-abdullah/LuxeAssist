from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate , login , logout
from .models import Profile
from django.db import IntegrityError
from services.models import Review

# Create your views here.

def register_page_view(request:HttpRequest):
    message = None

    if request.method == "POST":
        try:
            # Create a new user
            user = User.objects.create_user(username=request.POST["username"], first_name = request.POST["first_name"], last_name = request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            profile = Profile(user=user, city=request.POST["city"], address=request.POST["address"], phone_number=request.POST["phone_number"])
            profile.save()

            if "user" in request.GET:
               #add to group
               group_concerge, created = Group.objects.get_or_create(name="conceirge")

               user.groups.add(group_concerge)
               user.is_active = False
               user.save()


            return redirect("accounts:login_page_view")
        except IntegrityError as e:
           message = f"Please select another username"
        except Exception as e:
          print(e)
          message = f"something went wrong {e}"


    return render(request, "accounts/register.html",{"message":message})


def login_page_view(request: HttpRequest):
    message = None

    if request.method == "POST":
        #firt : authenticate the user data
        user = authenticate(request,username = request.POST["username"], password = request.POST["password"])

        if user:
            #second: login the user
            login(request, user)
            return redirect("main:home_view")
        
        else:
           message = "Please provide correct username and password"


    return render(request, "accounts/login.html",{"message":message})


def logout_page_view(request: HttpRequest):
    
    #log out the user
    if request.user.is_authenticated:
        logout(request)    

    return redirect("accounts:login_page_view")
    

def user_profile_page_view(request: HttpRequest , user_id):
    if  not request.user.is_authenticated :
        return render(request,"main/user_not_found.html", status=401)
    try:
      user = User.objects.get(id = user_id)
      user_reviews = Review.objects.filter(user = request.user)
        
    except:
       return render(request ,"main/user_not_found.html")
        
    return render(request,"accounts/profile.html",{"user":user , "reviews":user_reviews})
    

def update_profile_page_view(request: HttpRequest):
   message = None

   if  not request.user.is_authenticated :
        return render(request,"main/user_not_found.html", status=401)

   if request.method == "POST": 
    try:
        if request.user.is_authenticated:
            user: User = request.user
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.email=request.POST["email"]
            user.save()

            profile : Profile = request.user.profile

            if "avatar" in request.FILES:
                profile.avatar = request.FILES["avatar"]

            profile.city= request.POST["city"]
            profile.address= request.POST["address"]
            profile.phone_number= request.POST["phone_number"]
            profile.gender = request.POST["gender"]
            profile.nationality = request.POST["nationality"]
            profile.about = request.POST["about"]
            profile.save()

            return redirect("accounts:user_profile_page_view", user_id = request.user.id)
                
        else:
            return redirect("accounts:login_page_view")

    except Exception as e:
        message = f"A typing error occurred {e}"

            
   return render(request, "accounts/update.html",{"message":message})
            