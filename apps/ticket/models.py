from django.db import models
import jdatetime
from django.utils.html import mark_safe
from django_jalali.db import models as jmodels

from apps import utilities
from apps.accounts.models import User


class TicketType(models.Model):
    name = models.CharField(max_length=1000, verbose_name="نام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نوع تیکت"
        verbose_name_plural = "انواع تیکت"


class Ticket(models.Model):
    PRIORITY_CHOICES = (('INSTANTANEOUS', 'خیلی عجله دارم'), ('MEDIUM', 'عجله دارم'), ('LOW', 'عجله ندارم'))
    title = models.CharField(max_length=1000, verbose_name="عنوان")
    description = models.TextField(verbose_name='متن')
    full_name = models.CharField(max_length=1000, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=1000, verbose_name="ایمیل")
    area_code = models.CharField(max_length=5, verbose_name="پیش شماره")
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن")
    created_at = jmodels.jDateField(default=jdatetime.date.today(), verbose_name="تاریخ ایجاد")
    priority = models.CharField(choices=PRIORITY_CHOICES, default='LOW', max_length=13, verbose_name="اولویت")
    is_read = models.BooleanField(default=False, verbose_name="وضعیت خواندن(خوانده/خوانده نشده)")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="tickets")
    ticket_ans = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="پاسخ به", related_name='answer', null=True,
                               blank=True)
    type = models.ForeignKey(TicketType, on_delete=models.CASCADE, verbose_name="نوع تیکت", related_name="tickets")
    is_active = models.BooleanField(default=False, verbose_name="وضعیت")
    def get_priority_display_value(self):
        return self.get_priority_display()

    def __str__(self):
        return f'{self.user.name} {self.user.family}: {self.title}'

    def get_item(self):
        return mark_safe(
            f'<a style="border-radius: 5px;background-color: #417690;padding: 5px 11px;font-weight: 450; color:#fff;" href="{utilities.base_url}admin/ticket/ticketitem/?ticket_id={self.id}">فایلها</a>')

    get_item.short_description = 'مشاهده فایلها'
    get_item.allow_tags = True

    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"


class TicketItem(models.Model):
    file = models.FileField(upload_to='tickets/', verbose_name='فایل')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="تیکت", related_name="ticket_items")

    def __str__(self):
        return f'{self.ticket}:Ticket Item {self.id}'

    class Meta:
        verbose_name = "آیتم تیکت"
        verbose_name_plural = "آیتم های تیکت"
