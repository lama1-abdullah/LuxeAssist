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
        #try:

            contact = Contact(user=request.user, type=request.POST["type"], content=request.POST["content"])
            contact.save()

            return redirect("main:contact_view")
        #except:
            return render(request, "main/user_not_found.html")
    
    user_contact= Contact.objects.filter(user= request.user)
    
    return render(request, "main/contact.html", {"categories": Contact.categories ,"user_contact" : user_contact}) 



def payment_view(request: HttpRequest ,requests_id):
    msg=None
    if not request.user.is_authenticated and request.user.groups.exists and request.user.is_superuser and request.user.is_staff :
        return render(request,"main/user_not_found.html", status=401)
 
    requests=Request.objects.get(id=requests_id)
    
    if request.method=="POST":
        try:
            new_payment=Payment( requests=requests ,user=request.user, method_card=request.POST["method_card"], full_name=request.POST["full_name"], number_card=request.POST["number_card"],expiration_date=request.POST["expiration_date"], cvv = request.POST["cvv"])
            new_payment.save()
            subject = 'welcome to LuxeAssist world'

            message = f'Hi {request.user.first_name} {request.user.last_name}, Thank you for trusting us, your payment was completed successfully.\n Your order details:\nTitle:{requests.service.title}\nDescription:{requests.service.description}\nDate:{requests.date}\nPrice:{requests.request_price}\nSee you soon, dont forget to visit us again.'

            from_email = settings.EMAIL_HOST_USER


            recipient_list = [request.user.email]
            send_mail( subject=subject, message=message, from_email=from_email, recipient_list=recipient_list )
            return redirect("main:success_payment_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

    return render(request, "main/payment.html",{"requests": requests , "categories": Payment.categories ,"msg":msg}) 


def not_found_view(request: HttpRequest):

   return render(request, "main/user_not_found.html")



def display_all_contacts_view(request:HttpRequest):

    if  not request.user.is_superuser and not request.user.is_staff  :
            return render(request,"main/user_not_found.html", status=401)

    contacts = Contact.objects.all()
    return render(request, "main/display_all_contacts.html", {"contacts": contacts})
  


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
     
    if not request.user.is_superuser :
        return render(request,"main/user_not_found.html", status=401)

    return render(request,"main/admin_page.html")


def success_payment_view(request: HttpRequest):
    
    return render(request, "main/success_payment.html")