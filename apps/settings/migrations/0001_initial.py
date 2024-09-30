# Generated by Django 5.1.1 on 2024-09-30 09:56

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_text', models.CharField(blank=True, help_text='متن کپی\u200cرایت در فوتر', max_length=500, null=True)),
                ('background_color', colorfield.fields.ColorField(default='#000000', help_text='رنگ پس\u200cزمینه فوتر', image_field=None, max_length=25, samples=None)),
                ('text_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='رنگ متن فوتر', image_field=None, max_length=25, samples=None)),
                ('show_newsletter_signup', models.BooleanField(default=True, help_text='آیا فرم ثبت \u200cنام خبرنامه نمایش داده شود؟')),
                ('show_social_links', models.BooleanField(default=True, help_text='آیا لینک \u200cهای شبکه\u200cهای اجتماعی نمایش داده شود؟')),
                ('is_active', models.BooleanField(default=True, help_text='فوتری که انتخاب کنید نمایش داده میشود . توجه شما میتوانید یک فوتر انتخاب کنید', verbose_name='on/off')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='header/logo/', verbose_name='لوگوی سایت')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='عنوان سایت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیح مختصر')),
                ('color', colorfield.fields.ColorField(blank=True, default='#FF0000', image_field=None, max_length=25, null=True, samples=None, verbose_name='رنگ متن')),
                ('background_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', image_field=None, max_length=25, null=True, samples=None, verbose_name='رنگ زمینه')),
                ('is_active', models.BooleanField(default=True, help_text='هدر که انتخاب کنید نمایش داده میشود . توجه شما میتوانید یک هدر انتخاب کنید', verbose_name='on/off')),
            ],
        ),
        migrations.CreateModel(
            name='MetaHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('name', 'name'), ('charset', 'charset'), ('property', 'property')], max_length=50, null=True, verbose_name='نوع متا')),
                ('content', models.TextField(blank=True, null=True, verbose_name='محتوی')),
                ('key', models.CharField(blank=True, max_length=500, null=True, verbose_name='کلید متا')),
            ],
        ),
        migrations.CreateModel(
            name='SiteTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_theme', models.CharField(default='theme1', max_length=50, verbose_name='انتخاب قالب')),
                ('is_active', models.BooleanField(default=True, help_text='قالب که انتخاب کنید نمایش داده میشود . توجه شما میتوانید یک قالب انتخاب کنید', verbose_name='on/off')),
            ],
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان لینک', max_length=200)),
                ('url', models.URLField(help_text='آدرس URL لینک')),
                ('is_external', models.BooleanField(default=False, help_text='آیا لینک خارجی است؟')),
                ('is_active', models.BooleanField(default=True, verbose_name='on/off')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='settings.footersettings', verbose_name='انتخاب فوتر')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام منو')),
                ('is_active', models.BooleanField(default=True, help_text='منوی فعال در سایت نمایش داده می\u200cشود.', verbose_name='فعال بودن منو')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.sitetemplate', verbose_name='قالب')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(help_text='نام شبکه اجتماعی (مثلاً Instagram، Twitter)', max_length=100)),
                ('url', models.URLField(help_text='آدرس پروفایل شبکه اجتماعی')),
                ('icon', models.ImageField(blank=True, help_text='آیکون شبکه اجتماعی', null=True, upload_to='footer/social_icons/')),
                ('is_active', models.BooleanField(default=True, verbose_name='on/off')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='settings.footersettings')),
            ],
        ),
    ]
