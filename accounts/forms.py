from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    email = forms.EmailField(
        label = "ایمیل",
        widget = forms.EmailInput(attrs = {"class": "form-control", "placeholder": "ایمیل را وارد کنید"})
    )
    password = forms.CharField(
        label = "رمز عبور",
        widget = forms.PasswordInput(attrs = {"class": "form-control", "placeholder": "رمز عبور را وارد کنید"})
    )
    confirm_password = forms.CharField(
        label = "تکرار رمز عبور",
        widget = forms.PasswordInput(attrs = {"class": "form-control", "placeholder": "تکرار رمز عبور را وارد کنید"})
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("ایمیل وارد شده از قبل ثبت شده است")
        return email

    def clean(self):
        cleaned_date = super().clean()
        password = cleaned_date.get("password")
        confirm_password = cleaned_date.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("رمز عبور یا تایید رمز عبور یکسان نیستیند")
        return cleaned_date

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