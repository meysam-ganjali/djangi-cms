from django.contrib import admin
from .models import Ticket, TicketItem, TicketType
from django.utils.safestring import mark_safe


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class TicketItemInstanceAdminInline(admin.TabularInline):
    model = TicketItem
    extra = 3


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    list_display = (
        'title', 'type', 'user', 'get_priority', 'full_name', 'get_phone', 'get_item_count','count_answer','get_item')
    inlines = [TicketItemInstanceAdminInline]
    def count_answer(self,obj):
        return obj.answer.count()

    count_answer.short_description = 'تعداد پاسخ'
    def get_priority(self, obj):
        return obj.get_priority_display_value()

    def get_phone(self, obj):
        return f'({obj.area_code})-{obj.phone}'

    def get_item_count(self, obj):
        return obj.ticket_items.count()

    get_phone.short_description = 'تلفن'
    get_priority.short_description = 'اولویت'
    get_item_count.short_description = 'تعداد فایل ارسالی'


@admin.register(TicketItem)
class TicketItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'get_file_link')

    def get_file_link(self, obj):
        if obj.file:
            return mark_safe(
                f'<a style="border-radius: 5px;background-color: #417690;padding: 5px 11px;font-weight: 450; color:#fff;" href="{obj.file.url}" target="_blank">نمایش فایل</a>')
        return 'فایلی موجود نیست'
