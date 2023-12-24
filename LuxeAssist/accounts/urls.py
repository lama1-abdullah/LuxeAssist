from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_page_view, name="register_page_view"),
    path("login/", views.login_page_view, name="login_page_view"),
    path("logout/", views.logout_page_view, name="logout_page_view"),
    path("profile/<user_id>/", views.user_profile_page_view, name="user_profile_page_view"),
    path("update/", views.update_profile_page_view, name="update_profile_page_view"),
]