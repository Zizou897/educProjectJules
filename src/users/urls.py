from django.urls import path
from .views import UserLoginView, UserLogoutView, ProfileView

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profil/", ProfileView.as_view(), name="profile"),
]
