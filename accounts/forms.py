from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import CustomUser



User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label = "ایمیل",
        widget = forms.EmailInput(attrs = {"class": "form-control", "placeholder": "ایمیل را وارد کنید"})
    )
    password1 = forms.CharField(
        label = "رمز عبور",
        widget = forms.PasswordInput(attrs = {"class": "form-control", "placeholder": "رمز عبور را وارد کنید"})
    )
    password2 = forms.CharField(
        label = "تکرار رمز عبور",
        widget = forms.PasswordInput(attrs = {"class": "form-control", "placeholder": "تکرار رمز عبور را وارد کنید"})
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("ایمیل وارد شده از قبل ثبت شده است")
        return email

    def clean(self):
        cleaned_date = super().clean()
        password = cleaned_date.get("password1")
        confirm_password = cleaned_date.get("password2")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("رمز عبور یا تایید رمز عبور یکسان نیستیند")
        return cleaned_date

    def save(self, commit=True):
        user = super().save(commit=False)  # ایجاد یک نمونه از مدل کاربر که هنوز ذخیره نشده
        user.set_password(self.cleaned_data["password1"])  # هش کردن رمز عبور
        if commit:
            user.save()
        return user


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label = "ایمیل",
        widget = forms.EmailInput(attrs = {"class": "form-control", "placeholder": "ایمیل را وارد کنید"}),
        error_messages = {
            'required': 'لطفاً ایمیل خود را وارد کنید.',
            'invalid': 'ایمیل وارد شده معتبر نیست.'
        }
    )
    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'رمز عبور خود را وارد کنید'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("ایمیل وارد شده وجود ندارد.")
        return email