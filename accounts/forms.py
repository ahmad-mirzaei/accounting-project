from django import forms
from django.contrib.auth.forms import AuthenticationForm


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label = "ایمیل",
        widget = forms.EmailInput(attrs = {"class": "form-control", "placeholder": "ایمیل را وارد کنید"})
    )