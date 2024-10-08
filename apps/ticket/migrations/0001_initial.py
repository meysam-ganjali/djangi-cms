# Generated by Django 5.1.1 on 2024-09-30 13:21

import datetime
import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'نوع تیکت',
                'verbose_name_plural': 'انواع تیکت',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='متن')),
                ('full_name', models.CharField(max_length=1000, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=1000, verbose_name='ایمیل')),
                ('area_code', models.CharField(max_length=5, verbose_name='پیش شماره')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تلفن')),
                ('created_at', django_jalali.db.models.jDateField(default=datetime.date(2024, 9, 30), verbose_name='تاریخ ایجاد')),
                ('priority', models.CharField(choices=[('INSTANTANEOUS', 'خیلی عجله دارم'), ('MEDIUM', 'عجله دارم'), ('LOW', 'عجله ندارم')], default='LOW', max_length=13, verbose_name='اولویت')),
                ('is_read', models.BooleanField(default=False, verbose_name='وضعیت خواندن(خوانده/خوانده نشده)')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('ticket_ans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='ticket.ticket', verbose_name='پاسخ به')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ticket.tickettype', verbose_name='نوع تیکت')),
            ],
            options={
                'verbose_name': 'تیکت',
                'verbose_name_plural': 'تیکت ها',
            },
        ),
        migrations.CreateModel(
            name='TicketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='tickets/', verbose_name='فایل')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_items', to='ticket.ticket', verbose_name='تیکت')),
            ],
            options={
                'verbose_name': 'آیتم تیکت',
                'verbose_name_plural': 'آیتم های تیکت',
            },
        ),
    ]
