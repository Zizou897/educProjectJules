from django.contrib import admin
from django.urls import path, include
from .views import DashboardView, root_redirect_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),

    # Core
    path("", root_redirect_view, name="root"),
    path("dashboard/", login_required(DashboardView.as_view()), name="dashboard"),

    # Apps
    path("", include("users.urls", namespace="users")),
    path("", include("academics.urls", namespace="academics")),
    path("", include("communication.urls", namespace="communication")),
    path("", include("administration.urls", namespace="administration")),
    path("", include("events.urls", namespace="events")),
]
