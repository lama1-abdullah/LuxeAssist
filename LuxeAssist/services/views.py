from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .models import TypeService
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

    return render(request , "services/details_typeService.html",{"typeService":typeServices})

def add_service_view(request:HttpRequest):
    pass