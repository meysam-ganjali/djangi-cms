from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from django.utils.html import mark_safe

LOCATION = (
    ('top_top', 'بالا - بالا'),
    ('top_center', 'بالا - وسط'),
    ('top_bottom', 'بالا - پایین'),
    ('center_top', 'وسط - بالا'),
    ('center_center', 'وسط - وسط'),
    ('center_bottom', 'وسط - پایین'),
    ('bottom_top', 'پایین - بالا'),
    ('bottom_center', 'پایین - وسط'),
    ('bottom_bottom', 'پایین - پایین'))

BANNER_SIZE = (
    ('col-sm-1', '8.33% درحالت گوشی'),
    ('col-sm-2', '16.66% درحالت گوشی'),
    ('col-sm-3', '24.99% درحالت گوشی'),
    ('col-sm-4', '33.32% درحالت گوشی'),
    ('col-sm-5', '41.65% درحالت گوشی'),
    ('col-sm-6', '49.98% درحالت گوشی'),
    ('col-sm-7', '58.31% درحالت گوشی'),
    ('col-sm-8', '66.64% درحالت گوشی'),
    ('col-sm-9', '74.97% درحالت گوشی'),
    ('col-sm-10', '83.3% درحالت گوشی'),
    ('col-sm-11', '91.63% درحالت گوشی'),
    ('col-sm-12', '100% درحالت گوشی'),
    ('col-md-1', '8.33% درحالت تبلت'),
    ('col-md-2', '16.66% درحالت تبلت'),
    ('col-md-3', '24.99% درحالت تبلت'),
    ('col-md-4', '33.32% درحالت تبلت'),
    ('col-md-5', '41.65% درحالت تبلت'),
    ('col-md-6', '49.98% درحالت تبلت'),
    ('col-md-7', '58.31% درحالت تبلت'),
    ('col-md-8', '66.64% درحالت تبلت'),
    ('col-md-9', '74.97% درحالت تبلت'),
    ('col-md-10', '83.3% درحالت تبلت'),
    ('col-md-11', '91.63% درحالت تبلت'),
    ('col-md-12', '100% درحالت تبلت'),
    ('col-lg-1', '8.33% درحالت مانیتور'),
    ('col-lg-2', '16.66% درحالت مانیتور'),
    ('col-lg-3', '24.99% درحالت مانیتور'),
    ('col-lg-4', '33.32% درحالت مانیتور'),
    ('col-lg-5', '41.65% درحالت مانیتور'),
    ('col-lg-6', '49.98% درحالت مانیتور'),
    ('col-lg-7', '58.31% درحالت مانیتور'),
    ('col-lg-8', '66.64% درحالت مانیتور'),
    ('col-lg-9', '74.97% درحالت مانیتور'),
    ('col-lg-10', '83.3% درحالت مانیتور'),
    ('col-lg-11', '91.63% درحالت مانیتور'),
    ('col-lg-12', '100% درحالت مانیتور'),

)


class Banner(models.Model):
    location = models.CharField(max_length=250, choices=LOCATION, default='top_top', verbose_name='مکان نمایش')
    title = models.CharField(max_length=250, verbose_name='عنوان بنر')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    badge1 = models.CharField(max_length=250, verbose_name='تیکه متن 1', null=True, blank=True)
    badge2 = models.CharField(max_length=250, verbose_name='تیکه متن 2', null=True, blank=True)
    badge3 = models.CharField(max_length=250, verbose_name='تیکه متن 3', null=True, blank=True)
    picture = models.ImageField(upload_to='banners/', verbose_name='تصویر')
    picture_alt = models.CharField(max_length=250, blank=True, null=True, verbose_name='متن جایگزین تصویر')
    picture_title = models.CharField(max_length=250, blank=True, null=True, verbose_name='عنوان تصویر')
    width = models.IntegerField(null=True, blank=True, verbose_name='عرض تصویر')
    height = models.IntegerField(null=True, blank=True, verbose_name='ارتفاع تصوبر')
    link = models.URLField(max_length=600, blank=True, null=True, verbose_name='لینک')
    link_title = models.CharField(max_length=250, blank=True, null=True, verbose_name='عنوان لینک')
    is_active = models.BooleanField(default=True, verbose_name='وضعیت')
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'

    def get_banner_img(self):
        if self.picture:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.picture)

    get_banner_img.short_description = 'تصویر'
    get_banner_img.allow_tags = True


class BannerSize(models.Model):
    size = models.CharField(choices=BANNER_SIZE, max_length=255, verbose_name='اندازه')
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE,related_name='banner_size', verbose_name='انتخاب بنر')
