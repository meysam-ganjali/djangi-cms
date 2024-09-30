from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from django.utils.html import mark_safe

from apps import utilities

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


class Slider(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name='عنوان اسلایدر')
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')
    delay = models.IntegerField(blank=True, null=True, verbose_name='مدت زمان تعویض')
    auto_play = models.BooleanField(default=True, verbose_name='شروع خودکار')
    type = models.CharField(choices=LOCATION, max_length=250, default='top_top', verbose_name='مکان نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title

    def get_item(self):
        return mark_safe(
            f'<a style="border-radius: 5px;background-color: #417690;padding: 5px 11px;font-weight: 450; color:#fff;" href="{utilities.base_url}admin/slider/slideritem/?slider_id={self.id}">دیدن اسلاید ها</a>')

    get_item.short_description = ''


class SliderItem(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name='عنوان اسلایدر')
    description = models.TextField( blank=True, null=True, verbose_name='توضیحات اسلایدر')
    link = models.URLField(max_length=600, blank=True, null=True, verbose_name='لینک')
    link_title = models.CharField(max_length=250, blank=True, null=True, verbose_name='عنوان لینک')
    picture = models.ImageField(upload_to='sliders/', verbose_name='عکس اسلایدر')
    picture_alt = models.CharField(max_length=250, blank=True, null=True, verbose_name='متن جایگزین')
    picture_title = models.CharField(max_length=250, blank=True, null=True, verbose_name='عنوان تصویر')
    width = models.IntegerField(null=True, blank=True, verbose_name='عرض تصویر')
    height = models.IntegerField(null=True, blank=True, verbose_name='ارتفاع تصوبر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, verbose_name='اسلایدر', related_name='slider_items')

    class Meta:
        verbose_name = 'آیتم اسلایدر'
        verbose_name_plural = 'آیتم اسلایدر ها'

    def __str__(self):
        return self.title

    def get_slide_img(self):
        return mark_safe(
            '<img src="/media/%s" width="150" height="70" style="border-radius:5px;" />' % self.picture)

    get_slide_img.short_description = 'تصویر'
    get_slide_img.allow_tags = True


