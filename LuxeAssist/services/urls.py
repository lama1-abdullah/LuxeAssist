from django.urls import path
from . import views


app_name = "services"

urlpatterns = [
    path('add/', views.add_typeService_view , name="add_typeService_view"),
    path('home/', views.home_services_view, name="home_services_view")
]