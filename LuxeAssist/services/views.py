from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User,Group
from .models import TypeService , Service, Review
from accounts.models import Profile
# Create your views here.

### Type Service View

def add_typeService_view(request:HttpRequest):
    msg=None
    if  not request.user.is_superuser and not request.user.is_staff :
            return render(request,"main/user_not_found.html", status=401)
    
    if request.method=="POST":
        try:
            new_service=TypeService(title=request.POST["title"],description=request.POST["description"], image=request.FILES["image"])
            new_service.save()
            return redirect("main:home_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"
        
    return render(request,"services/add_typeService.html" ,{"msg":msg})


def details_typeService_view(request:HttpRequest, typeService_id):
    msg=None
    
    try:
        typeServices=TypeService.objects.get(id=typeService_id)
        services=Service.objects.filter(type_service=typeServices)

    except Exception as e:
        msg=f"Sorry, something went wrong. Try again later {e}"

    return render(request , "services/details_typeService.html",{"typeService":typeServices , "services":services ,"msg":msg})

def all_serviceType_admin_viwe(request:HttpRequest):

    typeServices=TypeService.objects.all()

    return render(request , "services/all_serviceType_admin.html",{"typeService":typeServices})

def update_typeService_view(request:HttpRequest,typeService_id):
    msg=None
    if  not request.user.is_superuser and not request.user.is_staff :
        return render(request,"main/user_not_found.html", status=401)
    
    typeService= TypeService.objects.get(id=typeService_id)

    if request.method=="POST":
        try:
        
            typeService.title=request.POST["title"]
            typeService.description=request.POST["description"]
            if "image" in request.FILES:
                typeService.image=request.FILES["image"]
            typeService.save()

            return redirect("services:all_serviceType_admin_viwe") 
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"
        

        
    return render(request,"services/update_typeServices.html",{"typeService":typeService ,"msg":msg})


def delete_services_views(request:HttpRequest, typeService_id):

    if  not request.user.is_superuser and not request.user.is_staff :
        return render(request,"main/user_not_found.html", status=401)

    typeService= TypeService.objects.get(id = typeService_id)
    typeService.delete()
    return redirect("services:all_serviceType_admin_viwe")


### Service View

def add_service_view(request:HttpRequest):
    msg=None
    service_types = TypeService.objects.all()

    if not request.user.has_perm("services.add_service"): #not work with admin 
        return render(request,"main/user_not_found.html", status=401) 

    if request.method== "POST":
        try:
            typeservices=TypeService.objects.get(id=request.POST["type"])
            new_service=Service(user=request.user, type_service=typeservices , title=request.POST["title"],description=request.POST["description"], image=request.FILES["image"] , initial_price=request.POST["initial_price"])
            new_service.save()

            return redirect("services:details_typeService_view", typeService_id=typeservices.id)
        except Exception as e:
            msg=f"An error occured, please fill in all fields and try again . {e}"

    
    return render(request , "services/add_service.html", { "service_types" : service_types ,"msg": msg})

def details_service_view(request:HttpRequest, service_id):
    msg=None
    try:
        service=Service.objects.get(id=service_id)
        if request.method=="POST":
            try:
                reviews=Review(services=service,user=request.user,rating=request.POST["rating"],comment=request.POST["comment"])
                reviews.save()
            except Exception as e:
                msg=f"Sorry, something went wrong. Try again later {e}"

        reviews=Review.objects.filter(services=service)

        return render(request , "services/details_services.html",{"service":service , "reviews":reviews ,"msg":msg})
    except Exception as e:
        return redirect("main:not_found_view")


def update_service_view(request:HttpRequest, service_id):
    msg=None
    service=Service.objects.get(id=service_id)

    if  not request.user.has_perm("services.change_service"):#not work with admin
        return render(request,"main/user_not_found.html", status=401)   
    if request.method=="POST":

        try:

            service.title=request.POST["title"]
            service.description=request.POST["description"] 
            if "image" in request.FILES:
                service.image=request.FILES["image"]
            service.initial_price=request.POST["initial_price"]
            service.save()

            return redirect("services:conceirge_services_view")
        except Exception as e:
            msg=f"An error occured, please fill in all fields and try again . {e}"
        
    
    return render(request,"services/update_service.html",{"service": service,"msg":msg })

def delete_servicesConcierge_views(request:HttpRequest, service_id):
    if  not request.user.has_perm("services.delete_service"):#not work with admin
        return render(request,"main/user_not_found.html", status=401) 
    
    service=Service.objects.get(id=service_id)
    service.delete()
    return redirect("services:conceirge_services_view")


def all_servicesProvider_view (request:HttpRequest):

    msg=None
    if  not request.user.is_superuser and not request.user.is_staff:
            return render(request,"main/user_not_found.html", status=401)
    try:
        coceirge_users = User.objects.filter(groups__name="conceirge")
    except Exception as e:
        msg=f"Sorry, something went wrong. Try again later {e}"


    return render(request,"services/all_services_rovider.html", {"coceirge_users": coceirge_users,"msg":msg})


def activate_conceirge_viwe(request:HttpRequest,user_id):
    if  not request.user.is_superuser :
        return render(request,"main/user_not_found.html", status=401)
    
    user =  User.objects.get(id = user_id)
    user.is_active = True
    user.save()
    
    return redirect("services:all_servicesProvider_view")


def deactivate_conceirge_viwe(request:HttpRequest,user_id):
    if  not request.user.is_superuser :
        return render(request,"main/user_not_found.html", status=401)
    
    user =  User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return redirect("services:all_servicesProvider_view")



def all_services_admin_view(request:HttpRequest):
    msg=None
    if  not request.user.is_superuser and not request.user.is_staff  :
            return render(request,"main/user_not_found.html", status=401)
    try:
        all_services = Service.objects.all()
    except Exception as e:
        msg=f"Sorry, something went wrong. Try again later {e}"

    return render (request,"services/all_services_admin.html",{"all_services":all_services,"msg":msg})


def delete_services_admin_views(request:HttpRequest, service_id):

    if  not request.user.is_superuser :
            return render(request,"main/user_not_found.html", status=401)

    service=Service.objects.get(id=service_id)
    service.delete()
    return redirect("services:all_services_admin_view")




def conceirge_services_view(request:HttpRequest):
    msg=None
    if not request.user.has_perm("services.add_service"): #not work with admin 
        return render(request,"main/user_not_found.html", status=401)
    try:
        service = Service.objects.filter(user = request.user)
    except Exception as e:
        msg=f"Sorry, something went wrong. Try again later {e}"



    return render(request , 'services/conceirge_services.html', {"service":service ,"msg":msg})

