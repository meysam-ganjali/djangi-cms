# Generated by Django 5.1.1 on 2024-10-09 07:49

import datetime
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=django_jalali.db.models.jDateField(default=datetime.date(2024, 10, 9), verbose_name='تاریخ ساخت مقاله'),
        ),
    ]
