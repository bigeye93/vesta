from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    list_display = ("username", "email", "coe", "part", "superuser")
    list_filter = ("coe", "part")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("avatar", "empoyee_number", "coe", "part", "superuser",)},
        ),
    )
