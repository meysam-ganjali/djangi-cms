from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','family','user_phone','is_active','is_admin')
    list_editable = ('is_active','is_admin')
    list_filter = ('is_active','is_admin')
    search_fields = ('user_phone','name','family')
