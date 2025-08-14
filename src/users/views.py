from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserLoginView(LoginView):
    template_name = "users/login.html"

class UserLogoutView(LogoutView):
    pass

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
