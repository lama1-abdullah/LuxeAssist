from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from.models import Payment , Contact
from request.models import Request



# Create your views here.
def home_view(request: HttpRequest):

    return render(request, "main/home.html")


def about_view(request: HttpRequest):

    return render(request, "main/about.html")


def contact_view(request: HttpRequest):

    if request.method=="POST":

        contact = Contact(user=request.user, type=request.POST["type"], content=request.POST["content"])
        contact.save()

        return redirect("main:home_view")
    
    return render(request, "main/contact.html", {"categories": Contact.categories}) 



def payment_view(request: HttpRequest ,requests_id):

  #try:
    requests=Request.objects.get(id=requests_id)
    
    if request.method=="POST":
        new_payment=Payment( requests=requests ,user=request.user, method_card=request.POST["method_card"], full_name=request.POST["full_name"], number_card=request.POST["number_card"],expiration_date=request.POST["expiration_date"], cvv = request.POST["cvv"])
        new_payment.save()
        return redirect("main:home_view")
  #except:
        #return render(request, "main/user_not_found.html")

    return render(request, "main/payment.html",{"requests": requests , "categories": Payment.categories}) 


def not_found_view(request: HttpRequest):

   return render(request, "main/user_not_found.html")



def display_all_contacts_view(request:HttpRequest):

    contacts = Contact.objects.all()
    return render(request, "main/display_all_contacts.html", {"contacts": contacts})

    # if request.user.is_staff:
    #     # User is a staff
    #     contacts = Contact.objects.all()
    #     return render(request, "main/display_all_contacts.html", {"contacts": contacts})
    # else:
    #     # User is not a staff 
    #     return render(request, "main/user_not_found.html")
