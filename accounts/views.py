from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import EmailLoginForm
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"user": request.user}
        return render(request, "base.html", context)


class CustomLoginView(LoginView):
    form_class = EmailLoginForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy("admin:index")
        return reverse_lazy("home")
