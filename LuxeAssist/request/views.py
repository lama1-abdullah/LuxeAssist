from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Request 
from services.models import Service
from .models import RequestComment 




def add_Request_view(request:HttpRequest, service_id):
        #if not request.user.is_authenticated:
              # return render(request, "", status=401)
        
    service = Service.objects.get(id = service_id)  
    if request.method == "POST":
        newRequest = Request(user = request.user, service = service, note = request.POST["note"], date = request.POST["date"], request_price = request.POST["request_price"])
        newRequest.save()
        return redirect("request:request_details_view", newRequest.id)
        

def user_requests_view(request: HttpRequest):
    # if request.user.is_authenticated and not request.user.is_superuser and request.user.is_staff :
    #    return render(request,"main/user_not_found.html", status=401)
   # try:
        
    requests = Request.objects.filter(user= request.user)

    return render(request, 'request/user_requests_view.html', {"requests" : requests})
    #except Exception as e:

      #  return render(request, "")
    

def concierge_requests_view(request: HttpRequest): 
    # if  not request.user.is_authenticated and not request.user.groups.exists :
    #     return render(request,"main/user_not_found.html", status=401)
   # try:
    services=Service.objects.filter(user=request.user)
    requests = Request.objects.filter(service__in= services)
    
    return render(request, 'request/concierge_requests_view.html', {"requests" : requests})
    #except Exception as e:

       # return render(request, "")
    

def admin_requests_view(request: HttpRequest):
    # if request.user.is_superuser and request.user.is_staff :
    #         return render(request,"main/user_not_found.html", status=401)
  # try: 
      requests = Request.objects.order_by('-date')
     
     
      return render(request ,"request/admin_requests_view.html" , {"requests" : requests})
   #except Exception as e:

       # return render(request, "")
   

def request_details_view(request: HttpRequest,requsets_id):
    requests = Request.objects.get(id =requsets_id)

    try:
       
        if request.method == "POST":
            new_Request = RequestComment(user = request.user, requests = requests, comment = request.POST["comment"])
            new_Request.save()
        requestComment=RequestComment.objects.filter(requests = requests)
       
    except Exception as e:
        return redirect("main:home_view")
        
    return render(request ,"request/request_details_view.html", {"requests":requests , "requestComment": requestComment})

     

def cancel_request_view(request: HttpRequest, requset_id):
    # if request.user.is_superuser and request.user.is_staff :
    #         return render(request,"main/user_not_found.html", status=401)
    
    try:
        requests = Request.objects.get(id = requset_id)
        requests.delete()
        return redirect("main:home_view")
        
    except  Exception as e:

        return render(request, "main/user_not_found.html")

def update_price_view(request:HttpRequest, requests_id):

    requests = Request.objects.get(id = requests_id) 

    if  not request.user.is_superuser and request.user.is_superuser and request.user.is_staff :
            return render(request,"main/user_not_found.html", status=401)
     
    if request.method == "POST":
        requests.request_price = request.POST["request_price"]
        requests.save()
        return redirect("request:request_details_view", requsets_id = requests.id)


def add_status_view(request: HttpRequest, requests_id):
    # if request.user.is_authenticated and not request.user.groups.exists :
    #     return render(request,"main/user_not_found.html", status=401)

    requests = Request.objects.get(id = requests_id)

    if request.method == "POST":
        requests.status = request.POST["status"]
        requests.save()
        return redirect("request:request_details_view",requsets_id = requests.id )
    
def new_requestConcierge_view(request: HttpRequest , requset_id):

    requests = Request.objects.get(id = requset_id) 

    return render (request, "request/new_requestConcierge_view.html", {"requests": requests})


def delete_request_admin_view(request: HttpRequest, requset_id):
    # if not request.user.is_superuser and request.user.is_staff :
    #     return render(request,"main/user_not_found.html", status=401)

    requsets=Request.objects.get(id=requset_id)
    requsets.delete()
    return redirect("request:admin_requests_view")
    


