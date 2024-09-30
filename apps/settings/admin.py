from django.contrib import admin
from .models import SiteTemplate, HeaderSettings, MetaHeader, FooterSettings, FooterLink, SocialLink


@admin.register(SiteTemplate)
class SiteTemplateAdmin(admin.ModelAdmin):
    list_display = ('get_theme_img','current_theme', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)


@admin.register(HeaderSettings)
class HeaderSettingsAdmin(admin.ModelAdmin):
    list_display = ('get_logo_img', 'title', 'is_active')
    list_editable = ('is_active',)


@admin.register(MetaHeader)
class MetaHeaderAdmin(admin.ModelAdmin):
    list_display = ('type', 'key', 'content')


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ('copyright_text', 'is_active', 'show_newsletter_signup', 'show_social_links')
    list_editable = ('is_active', 'show_newsletter_signup', 'show_social_links')


@admin.register(FooterLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('footer', 'title', 'url', 'is_external', 'is_active')
    list_editable = ('is_external', 'is_active')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('get_logo_img', 'platform', 'url', 'is_active')
    list_editable = ('is_active',)
