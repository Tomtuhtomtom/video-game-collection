from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Collection


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Collection)
