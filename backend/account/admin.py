from django.contrib import admin

from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password','friends')}),
        ('Permissions', {'fields': ('is_active', 'is_staff','is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (
            None,
        {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        },
        ),
    )
    list_display = ('name', 'email', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, AccountAdmin)
