from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
 # local
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "email",
        "username",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

admin.site.register(CustomUser,CustomUserAdmin)
