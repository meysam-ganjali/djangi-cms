from django.contrib import admin
from .models import Banner, BannerSize


class BannerSizeTabularInline(admin.StackedInline):
    model = BannerSize
    extra = 3


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_banner_img', 'link', 'register_date', 'is_active')
    list_filter = ('is_active', 'register_date')
    list_editable = ('is_active',)
    search_fields = ('title',)
    ordering = ('-register_date',)
    inlines = [BannerSizeTabularInline]
