from django.views.generic import TemplateView
from django.shortcuts import redirect


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

def root_redirect_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")
