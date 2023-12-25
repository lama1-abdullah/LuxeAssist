from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Request
from services.models import Service


def add_Request_view(request:HttpRequest, service_id):
        #if not request.user.is_authenticated:
              # return render(request, "", status=401)
        
    service = Service.objects.get(id = service_id)  
    if request.method == "POST":
        newRequest = Request(user = request.user, service = service, note = request.POST["note"], date = request.POST["date"], request_price = request.POST["request_price"])
        newRequest.save()
        return redirect("request:request_details_view", newRequest.id)
        

def user_requests_view(request: HttpRequest):
   # try:
        
    requests = Request.objects.filter(user= request.user)

    return render(request, 'request/user_requests_view.html', {"requests" : requests})
    #except Exception as e:

      #  return render(request, "")
    

def concierge_requests_view(request: HttpRequest): 
   # try:
        
       requests = Request.objects.filter(user = request.user)

       return render(request, 'request/concierge_requests_view.html', {"requests" : requests})
    #except Exception as e:

       # return render(request, "")
    

def admin_requests_view(request: HttpRequest):
  # try: 
      requests = Request.objects.order_by('-date')
     
     
      return render(request ,"request/admin_requests_view.html" , {"requests" : requests})
   #except Exception as e:

       # return render(request, "")
   

def request_details_view(request: HttpRequest):
    
    return render(request ,"request/request_details_view.html")


def cancel_request_view(request: HttpRequest, requset_id):
    ## try:
            request = Request.objects.get(id = requset_id)
            request.delete()
            return redirect("service:")
        
     ##except  Exception as e:

        ## return render(request, "")

