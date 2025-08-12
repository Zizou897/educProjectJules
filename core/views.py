from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('core:dashboard')

login_view = CustomLoginView.as_view()

class DashboardView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        if self.request.user.is_authenticated:
            role = self.request.user.role
            if role == 'ADMIN':
                return ['index.html']
            elif role == 'TEACHER':
                return ['dashboard-02.html']
            elif role == 'STUDENT':
                return ['dashboard-03.html']
            elif role == 'PARENT':
                return ['dashboard-03.html'] # Using the same for parents for now
        return ['index.html'] # Default for any other case

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import User
from .forms import CustomUserChangeForm

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user-profile.html'
    success_url = reverse_lazy('core:profile')

    def get_object(self, queryset=None):
        return self.request.user
