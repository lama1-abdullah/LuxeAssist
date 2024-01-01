from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from.models import Payment , Contact
from request.models import Request
from services.models import Service
from services.models import TypeService
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.
def home_view(request: HttpRequest):
    

    typeServices=TypeService.objects.all()

    return render(request, "main/home.html" , {"typeServices":typeServices})


def about_view(request: HttpRequest):

    return render(request, "main/about.html")


def contact_view(request: HttpRequest):

    if request.method=="POST":

        contact = Contact(user=request.user, type=request.POST["type"], content=request.POST["content"])
        contact.save()

        return redirect("main:contact_view")
    
    user_contact= Contact.objects.filter(user= request.user)
    
    return render(request, "main/contact.html", {"categories": Contact.categories ,"user_contact" : user_contact}) 




def payment_view(request: HttpRequest ,requests_id):

  #try:
    requests=Request.objects.get(id=requests_id)
    
    if request.method=="POST":
        new_payment=Payment( requests=requests ,user=request.user, method_card=request.POST["method_card"], full_name=request.POST["full_name"], number_card=request.POST["number_card"],expiration_date=request.POST["expiration_date"], cvv = request.POST["cvv"])
        new_payment.save()
        subject = 'welcome to GFG world'

        message = f'Hi {User.username}, thank you for registering in geeksforgeeks.'

        from_email = settings.EMAIL_HOST_USER

        recipient_list = [User.email ]
        send_mail( subject=subject, message=message, from_email=from_email, recipient_list=recipient_list )
        return redirect("main:success_payment_view")
  #except:
        #return render(request, "main/user_not_found.html")

    return render(request, "main/payment.html",{"requests": requests , "categories": Payment.categories}) 


def not_found_view(request: HttpRequest):

   return render(request, "main/user_not_found.html")



def display_all_contacts_view(request:HttpRequest):
    # message = None
    # if request.user.is_staff:
    contacts = Contact.objects.all()
    return render(request, "main/display_all_contacts.html", {"contacts": contacts})
    # else:
        # User is not a staff 
        # return render(request, "main/user_not_found.html")
  


def search_view(request: HttpRequest):
    
    if "search" in request.GET:

        keyword = request.GET["search"]
        services = Service.objects.filter(title__contains=keyword)
        print("dddd")
        
    else:
        services = Service.objects.all()

    print(services)
    return render(request, "main/searsh.html", {"services" : services })

def admin_page_view(request: HttpRequest):

    return render(request,"main/admin_page.html")

def success_payment_view(request: HttpRequest):

    return render(request, "main/success_payment.html")
