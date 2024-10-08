# Generated by Django 5.1.1 on 2024-10-09 07:49

import datetime
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='کد فعالسازی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2024, 10, 9), verbose_name='تاریخ ثبت نام'),
        ),
    ]
