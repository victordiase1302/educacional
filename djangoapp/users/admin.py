from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from users.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "cell_phone",
        "role",
        "is_active",
    ]
    list_display_links = "id", "email"
    list_editable = ("is_active",)
    search_fields = ["email", "role"]
    list_per_page = 20
    f = list(auth_admin.UserAdmin.fieldsets)
    f[1] = (
        "Personal Info",
        {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "role",
                "cell_phone"
            )
        },
    )
    fieldsets = tuple(f)

admin.site.unregister(Group)
