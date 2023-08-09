from django.contrib import admin
from django.contrib.auth import admin as django_user_admin

from .forms import UserChangeForm, UserCreationForm
from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    list_display = ("username", "email", "first_name",
                    "last_name", "is_staff", "is_active")
    fieldsets = django_user_admin.UserAdmin.fieldsets + (
        ('Personal data', {
         'fields': ("image", "gender", "phone", "recovery_email")}),
    )
