from django.contrib import admin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('get_user_img', 'user_phone', 'name', 'family', 'is_admin')
    search_fields = ('user_phone', 'name', 'family')
    readonly_fields = ('register_date',)

    fieldsets = (
        (None, {'fields': ('user_phone', 'password')}),
        ('اطلاعات شخصی', {'fields': ('name', 'family', 'image')}),
        ('دسترسی‌ها', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_phone', 'name', 'family', 'password1', 'password2', 'is_active', 'is_admin')}
        ),
    )

    ordering = ('user_phone',)
    filter_horizontal = ()
