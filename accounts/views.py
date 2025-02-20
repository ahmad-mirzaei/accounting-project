from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import EmailLoginForm, SignupForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import get_user_model

# Create your views here.



User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"user": request.user}
        return render(request, "base.html", context)


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  #  ذخیره‌ی کاربر در دیتابیس
            login(request, user)  # لاگین خودکار پس از ثبت‌نام
            return redirect("home")  #هدایت به صفحه‌ی اصلی پس از ثبت‌نام موفق
        return render(request, "accounts/signup.html", {"form": form})



class CustomLoginView(LoginView):
    form_class = EmailLoginForm
    template_name = "accounts/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy("admin:index")
        return reverse_lazy("home")
