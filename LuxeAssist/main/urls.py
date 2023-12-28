from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
   path("", views.home_view, name="home_view"),
   path("about/", views.about_view, name="about_view"),
   path("search/", views.search_view, name="search_view"),
   path("contact/", views.contact_view, name="contact_view"),
   path("payment/<requests_id>/", views.payment_view, name="payment_view"),
   path("not/", views.not_found_view, name="not_found_view"),
   path("display/all/contact/",views.display_all_contacts_view, name = "display_all_contacts_view")

]