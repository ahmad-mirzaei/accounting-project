from django.urls import path
from .views import CustomLoginView, HomeView, SignupView

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('signup/', SignupView.as_view(), name = "signup"),
    path('login/', CustomLoginView.as_view(), name = "login"),

]