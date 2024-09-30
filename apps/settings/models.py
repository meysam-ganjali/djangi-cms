from django.db import models
from colorfield.fields import ColorField
from django.utils.html import mark_safe


class SiteTemplate(models.Model):
    current_theme = models.CharField(max_length=50, default='theme1', verbose_name="انتخاب قالب")
    image = models.ImageField(upload_to='themes/', null=True, blank=True, verbose_name="عکس")
    is_active = models.BooleanField(default=True, help_text="قالب که انتخاب کنید نمایش داده میشود . توجه شما میتوانید یک قالب انتخاب کنید", verbose_name="on/off")

    def __str__(self):
        return self.current_theme

    def save(self, *args, **kwargs):
        if self.is_active:
            type(self).objects.filter(is_active=True).exclude(id=self.id).update(is_active=False)
        super().save(*args, **kwargs)

    def get_theme_img(self):
        if self.image:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.image)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_theme_img.short_description = ''
    get_theme_img.allow_tags = True

    class Meta:
        verbose_name = "تم"
        verbose_name_plural = "تم ها"


class HeaderSettings(models.Model):
    logo = models.ImageField(upload_to='header/logo/', null=True, blank=True, verbose_name="لوگوی سایت")
    title = models.CharField(max_length=500, null=True, blank=True, verbose_name="عنوان سایت")
    description = models.TextField(null=True, blank=True, verbose_name="توضیح مختصر")
    color = ColorField(default='#FF0000', verbose_name="رنگ متن", null=True, blank=True)
    background_color = ColorField(default='#FFFFFF', verbose_name="رنگ زمینه", null=True, blank=True)
    is_active = models.BooleanField(default=True, help_text="هدر که انتخاب کنید نمایش داده میشود . توجه شما میتوانید یک هدر انتخاب کنید", verbose_name="on/off")

    def __str__(self):
        return f'{self.title}'

    def get_logo_img(self):
        if self.logo:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.logo)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_logo_img.short_description = ''
    get_logo_img.allow_tags = True

    def save(self, *args, **kwargs):
        if self.is_active:
            type(self).objects.filter(is_active=True).exclude(id=self.id).update(is_active=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "تنظیم سربرگ"
        verbose_name_plural = "تنظیمات سربرگ"


class MetaHeader(models.Model):
    META_TYPE = (('name', 'name'), ('charset', 'charset'), ('property', 'property'))
    type = models.CharField(max_length=50, choices=META_TYPE, null=True, blank=True, verbose_name="نوع متا")
    content = models.TextField(null=True, blank=True, verbose_name="محتوی")
    key = models.CharField(max_length=500, null=True, blank=True, verbose_name="کلید متا")

    def __str__(self):
        return f'{self.type}-{self.key}'

    class Meta:
        verbose_name = "سئو سربرگ"
        verbose_name_plural = "سئو سربرگ"


class FooterSettings(models.Model):
    copyright_text = models.CharField(max_length=500, null=True, blank=True, help_text="متن کپی‌رایت در فوتر")
    background_color = ColorField(default='#000000', help_text="رنگ پس‌زمینه فوتر")
    text_color = ColorField(default='#FFFFFF', help_text="رنگ متن فوتر")
    show_newsletter_signup = models.BooleanField(default=True, help_text="آیا فرم ثبت ‌نام خبرنامه نمایش داده شود؟")
    show_social_links = models.BooleanField(default=True, help_text="آیا لینک ‌های شبکه‌های اجتماعی نمایش داده شود؟")
    is_active = models.BooleanField(default=True, help_text="فوتری که انتخاب کنید نمایش داده میشود . توجه شما میتوانید یک فوتر انتخاب کنید", verbose_name="on/off")

    def __str__(self):
        return f"{self.copyright_text}"

    def save(self, *args, **kwargs):
        if self.is_active:
            type(self).objects.filter(is_active=True).exclude(id=self.id).update(is_active=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "تنظیم فوتر"
        verbose_name_plural = "تنظیمات فوتر"


class FooterLink(models.Model):
    footer = models.ForeignKey(FooterSettings, related_name='links', on_delete=models.CASCADE, verbose_name="انتخاب فوتر")
    title = models.CharField(max_length=200, help_text="عنوان لینک")
    url = models.URLField(help_text="آدرس URL لینک")
    is_external = models.BooleanField(default=False, help_text="آیا لینک خارجی است؟")
    is_active = models.BooleanField(default=True, verbose_name="on/off")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لینک  فوتر"
        verbose_name_plural = "لینک های فوتر"


class SocialLink(models.Model):
    footer = models.ForeignKey(FooterSettings, related_name='social_links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=100, help_text="نام شبکه اجتماعی (مثلاً Instagram، Twitter)")
    url = models.URLField(help_text="آدرس پروفایل شبکه اجتماعی")
    icon = models.ImageField(upload_to='footer/social_icons/', null=True, blank=True, help_text="آیکون شبکه اجتماعی")
    is_active = models.BooleanField(default=True, verbose_name="on/off")

    def __str__(self):
        return self.platform

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"

    def get_logo_img(self):
        if self.icon:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.icon)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_logo_img.short_description = ''
    get_logo_img.allow_tags = True
