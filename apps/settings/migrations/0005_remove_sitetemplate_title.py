# Generated by Django 5.1.1 on 2024-09-30 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_footerlink_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitetemplate',
            name='title',
        ),
    ]
