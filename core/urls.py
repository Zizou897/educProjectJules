from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, DashboardView, ProfileView

app_name = 'core'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:login'), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profil/', ProfileView.as_view(), name='profile'),
]
