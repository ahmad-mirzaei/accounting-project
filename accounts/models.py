from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

# -------------------------------------------------------------------------

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("ایمیل اجباری است")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

# -------------------------------------------------------------------------

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique = True, verbose_name = "ایمیل")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
# -------------------------------------------------------------------------
