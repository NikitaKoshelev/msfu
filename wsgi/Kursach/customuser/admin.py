from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser
from .forms import CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('username', 'last_name', 'first_name',
                    'email', 'get_quantity_articles', 'karma', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('ava', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)},)
    )

    ordering = ('last_name', 'first_name',)

    def queryset(self, request):
        if request.user.is_superuser:
            return super(CustomUserAdmin, self).queryset(request)
        else:
            qs = super(CustomUserAdmin, self).queryset(request)
            return qs.filter(username=request.user)


admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
