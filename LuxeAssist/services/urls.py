from django.urls import path
from . import views


app_name = "services"

urlpatterns = [
    path('add/type', views.add_typeService_view , name="add_typeService_view"),
    path('home/', views.home_services_view, name="home_services_view"),
    path('type/details/<typeservice_id>',views.details_typeService_view, name="details_typeService_view"),
    path('update/type/<typeservice_id>',views.update_typeService_view, name="update_typeService_view"),
    path('delete/<typeservice_id>', views.delete_stable_views,name="delete_stable_views"),
    path('add/<typeservice_id>',views.add_service_view , name="add_service_view")
]