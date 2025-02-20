from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class EmailLoginForm(AuthenticationForm):
    email = forms.EmailField(
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