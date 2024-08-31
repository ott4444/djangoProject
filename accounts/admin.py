from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from .models import CustomUser, Account

# accounts/admin.py
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # Define the fields to be used for searching
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Define the fields to be used in the edit form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    form = UserCreationForm
    add_form = UserCreationForm
    ordering = ('username',)


admin.site.register(User, UserAdmin)
#admin.site.register(CustomUser)
#admin.site.register(Account)
