from django.urls import path
from . import views


app_name = "request"

urlpatterns = [
    path('<service_id>/add/service/', views.add_Request_view, name="add_Request_view"),
    path('user/requests/', views.user_requests_view, name="user_requests_view"),
    path('all/requests/', views.admin_requests_view , name ="admin_requests_view"),
    path('concierge/requests/', views.concierge_requests_view, name="concierge_requests_view"),
    path('details/request/<requsets_id>/', views.request_details_view, name= "request_details_view"),
    path('cancel/request/<requset_id>/', views.cancel_request_view, name="cancel_request_view"),
    path('update/request/<requests_id>/', views.update_price_view, name="update_price_view"),
    path('details/request/Concierge/<requset_id>/', views.request_detailsConcierge_view, name= "request_detailsConcierge_view"),
    path('update/status/<requests_id>/', views.add_status_view, name="add_status_view"),
    path('new/request/<requset_id>', views.new_requestConcierge_view, name="new_requestConcierge_view")
    
]