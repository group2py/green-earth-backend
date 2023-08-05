from django.contrib import admin
from django.contrib.auth import admin as django_user_admin

from .models import Users, Genders
from .forms import UserChangeForm, UserCreationForm

admin.site.register(Genders)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    list_display = ("email","first_name", "last_name", "is_staff", "is_active")
    fieldsets = django_user_admin.UserAdmin.fieldsets + (
        ('Personal data', {'fields': ("image", "gender", "phone", "recorevy_email")}),
    )