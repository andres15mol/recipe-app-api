"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUsuserAdmin

from core import models


class UserAdmin(BaseUsuserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email','name']


admin.site.register(models.User, UserAdmin)