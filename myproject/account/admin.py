from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

# DJANGO || Into settings.py >>> AUTH_USER_MODEL = account.User || (app.ClassModel)

# Class || Handle User Management trough the Django Admin panel
class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # DJANGO || Fields displayed into Django Admin Panel
    list_display = ('username', 'date_joined', 'last_login', 'is_admin', 'is_staff')

    # DJANGO || Specifed fields that can be updated or deleted | fieldsets = (('Name Example', {'fields': ('fields_name',)}),)
    fieldsets = ()

    # DJANGO || Additional fields during User registration
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'matricule', 'nom', 'prenom', 'adresse', 'cp', 'ville', 'dateEmbauche',)}),
    )

    # DJANGO || Keyword fields to add into Admin Panel searchbar
    search_field = ('matricule', 'username')

    # DJANGO || Fields that can not be modified
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()


# DJANGO || Add Account Model management to Django Admin panel
admin.site.register(User, AccountAdmin)
