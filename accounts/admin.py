from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("bio", "github", "linkedin", "profile_picture", "website", "location"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)