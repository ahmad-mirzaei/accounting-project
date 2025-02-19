from django.urls import path
from .views import CustomLoginView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('login/', CustomLoginView.as_view(), name = "login"),

]