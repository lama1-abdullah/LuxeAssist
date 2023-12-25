from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .models import TypeService , Service
# Create your views here.



def add_typeService_view(request:HttpRequest):

    if request.method=="POST":
        new_service=TypeService(title=request.POST["title"],description=request.POST["description"], image=request.FILES["image"])
        new_service.save()
        return redirect("services:home_services_view")
        
    return render(request,"services/add_typeService.html")




def home_services_view(request:HttpRequest):

    typeServices=TypeService.objects.all()

    return render(request, 'services/home_service.html', {"typeService":typeServices})





def details_typeService_view(request:HttpRequest, typeservice_id):

    typeServices=TypeService.objects.get(id=typeservice_id)
    services=Service.objects.filter(type_service=typeServices)
    return render(request , "services/details_typeService.html",{"typeService":typeServices , "services":services})





def update_typeService_view(request:HttpRequest,typeservice_id):
   
    typeService= TypeService.objects.get(id=typeservice_id)

    if request.method=="POST":
        
        typeService.title=request.POST["title"]
        typeService.description=request.POST["description"]
        typeService.image=request.FILES["image"]
        typeService.save()

        return redirect("services:details_typeService_view",typeservice_id=typeService.id)
        

        
    return render(request,"services/update_typeServices.html",{"typeService":typeService })



# ****************************************error in delete_stable_views and add_service_view***************************************************
def delete_stable_views(request:HttpRequest, typeService_id):
    typeService= TypeService.objects.get(id=typeService_id)
    typeService.delete()

    return redirect( "services:home_services_view")

def add_service_view(request:HttpRequest,typeservice_id):

    services=Service.objects.get(id=typeservice_id)

    if request.method== "POST":
        new_service=Service(user=request.user, type_service=services , title=request.POST["title"],description=request.POST["description"], image=request.FILES["image"] , initial_price=request.POST["initial_price"])
        new_service.save()

        return redirect("service:details_typeService_view", typeservice_id=services.id)

    
    return render(request , "services/add_service.html", {"service":services})





        
