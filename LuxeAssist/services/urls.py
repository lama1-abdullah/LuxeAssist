from django.urls import path
from . import views


app_name = "services"

urlpatterns = [
    path('add/type/', views.add_typeService_view , name="add_typeService_view"),
    path('home/', views.home_services_view, name="home_services_view"),
    path('type/details/<typeService_id>/',views.details_typeService_view, name="details_typeService_view"),
    path('update/type/<typeService_id>/',views.update_typeService_view, name="update_typeService_view"),
    path('delete/<typeService_id>/', views.delete_services_views,name="delete_services_views"),
    path('add/',views.add_service_view , name="add_service_view"),
    path('details/<service_id>/', views.details_service_view, name="details_service_view"),
    path('update/<service_id>/', views.update_service_view, name="update_service_view"),
    path('concierge/delete/<service_id>/',views.delete_servicesConcierge_views, name="delete_servicesConcierge_views"),
    path('all/services/provider/', views.all_servicesProvider_view , name="all_servicesProvider_view"),
    path('activate/user/<user_id>/',views.activate_conceirge_viwe, name = "activate_conceirge_viwe"),
    path('deactivate/user/<user_id>/',views.deactivate_conceirge_viwe, name = "deactivate_conceirge_viwe"),
    path('all/services/admin/', views.all_services_admin_view , name="all_services_admin_view"),
    path('delete/services/admin/', views.delete_services_admin_views , name="delete_services_admin_views"),
    path('all/service/concierge/', views.conceirge_services_view, name = "conceirge_services_view" ),

]