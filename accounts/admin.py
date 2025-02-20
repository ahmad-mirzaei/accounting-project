from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_active", "is_staff", "date_joined", ]
    search_fields = ["email", ]
    list_editable = ["is_active", ]
    list_filter = ["is_active", "is_staff", "date_joined"]

