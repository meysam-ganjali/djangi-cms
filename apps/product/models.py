import jdatetime
from ckeditor_uploader.fields import RichTextUploadingField
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.accounts.models import User


class Category(models.Model):
    title = models.CharField(max_length=1000, verbose_name='نام دسته بندی')
    slug = models.SlugField(unique=True, verbose_name='عنوان در آدرس')
    logo = models.ImageField(upload_to='categories/logos/', null=True, blank=True, verbose_name='لوگو')
    logo_alt = models.CharField(max_length=1000, blank=True, null=True, verbose_name='متن جایگزین لوگو')
    logo_title = models.CharField(max_length=1000, blank=True, null=True, verbose_name='عنوان لوگو')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='دسته بندی والد',
                               related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_logo_img(self):
        if self.logo:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.logo)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_logo_img.short_description = ''
    get_logo_img.allow_tags = True

    def get_sub_cat(self):
        return mark_safe(self.children.count())

    get_sub_cat.short_description = 'تعداد زیر گروه'
    get_sub_cat.allow_tags = True


class Product(models.Model):
    product_name = models.CharField(max_length=1000, verbose_name='نام محصول')
    product_cover = models.ImageField(upload_to='products/product_covers/', verbose_name='کاور محصول')
    product_cover_alt = models.CharField(max_length=100, verbose_name='متن جایگزین کاور')
    product_cover_title = models.CharField(max_length=100, verbose_name='عنوان کاور')
    slug = models.SlugField(unique=True, verbose_name='عنوان در آدرس')
    short_description = RichTextField(config_name='special', verbose_name='توضیحات اجمالی')
    long_description = RichTextUploadingField(config_name='special', verbose_name='توضیحات کامل')
    view_count = models.PositiveIntegerField(default=1)
    created_at = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ثبت محصول')
    updated_at = jmodels.jDateField(verbose_name='تاریخ آخرین بروزرسانی', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='وضعیت محصول : (فعال/غیرفعال)')
    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_categories(self):
        s = ''
        for i in self.productCategory_of_product.all():
            s += f'{i.category.title}-'
        return mark_safe('<small style="color:blue;">%s</small>' % s)

    get_categories.short_description = 'گروه'
    get_categories.allow_tags = True

    def get_product_img(self):
        if self.product_cover:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.product_cover)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_product_img.short_description = ''
    get_product_img.allow_tags = True


class ProductCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='دسته بندی',
                                 related_name='category_of_products')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productCategory_of_product',
                                verbose_name='محصول')

    def __str__(self):
        return f'{self.product} - {self.category}'

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'


class ProductAttribute(models.Model):
    attribute_value = models.CharField(max_length=1000, verbose_name='مقدار ویژگی')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productAttr_of_product',
                                verbose_name='محصول')
    attribute_name = models.CharField(max_length=300, verbose_name='نام ویژگی')

    def __str__(self):
        return f'{self.product} - {self.attribute_name} - {self.attribute_value}'

    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی محصولات'


class ProductTag(models.Model):
    tag_title = models.CharField(max_length=1000, verbose_name='عنوان تگ')
    slug = models.SlugField(unique=True, verbose_name='عنوان در نوار آدرس')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productTag_of_product',
                                verbose_name='محصول')

    def __str__(self):
        return f'{self.tag_title} - {self.product}'

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگهای محصول'


class ProductSeo(models.Model):
    SEO_TYPE = (('name', 'name'), ('property', 'property'))
    title = models.CharField(max_length=6000, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    type = models.CharField(max_length=1000, choices=SEO_TYPE, verbose_name='نوع متا تگ')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productSeo_of_product',
                                verbose_name='محصول')

    def __str__(self):
        return f'{self.product}: {self.title} - {self.content}'

    class Meta:
        verbose_name = 'سئو محصول'
        verbose_name_plural = 'سئو محصولات'


class ProductInventoryUnit(models.Model):
    unit_name = models.CharField(max_length=100, verbose_name='واحد شمارش')

    class Meta:
        verbose_name = 'واحد اندازه گیری'
        verbose_name_plural = 'واحدهای اندازه گیری'

    def __str__(self):
        return self.unit_name

class ProductInventory(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='تعداد محصول')
    product_sales_price = models.PositiveIntegerField(null=True, blank=True, verbose_name='قیمت فروش محصول')
    discount_percent = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='درصد تخفیف')
    created_at = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ثبت انبار')
    final_price = models.PositiveIntegerField(null=True, blank=True, help_text='این فیلد توسط سیستم پر میشود',
                                              verbose_name='قیمت نهایی')
    product_lable = models.CharField(max_length=500, default='', verbose_name='نام محصول در انبار')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_of_inventory',
                                       verbose_name='محصول')
    unit = models.ForeignKey(ProductInventoryUnit, on_delete=models.CASCADE, related_name='unit_of_inventory',
                             verbose_name='واحد شمارش')

    def __str__(self):
        return f'{self.product.product_name} - {self.product_sales_price} - {self.product_lable} > {self.final_price}'

    def save(self, *args, **kwargs):
        if self.discount_percent:
            discount_amount = self.product_sales_price * self.discount_percent / 100
            self.final_price = self.product_sales_price - discount_amount
        else:
            self.final_price = self.product_sales_price
        super().save(*args, **kwargs)

    def get_product_img(self):
        if self.product.product_cover:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.product.product_cover)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_product_img.short_description = ''
    get_product_img.allow_tags = True

    def get_unit(self):
        return self.unit.unit_name

    class Meta:
        verbose_name = 'انبار محصول '
        verbose_name_plural = ' انبار محصولات '


class ProductTimingDiscount(models.Model):
    start_time = jmodels.jDateField(verbose_name='تاریخ شروع تخفیف')
    day_count = models.IntegerField(verbose_name='تعداد روز تخفیف')
    end_time = jmodels.jDateField(help_text='این گزینه توسط سیستم پر میشود', null=True, blank=True,
                                  verbose_name='تاریخ پایان')
    discount = models.IntegerField(verbose_name='درصد تخفیف')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='محصول',
                                   related_name='product_timing_discount')
    product_inventory = models.OneToOneField(ProductInventory, null=True, blank=True, on_delete=models.CASCADE,
                                             related_name='product_timing_discount', verbose_name='انبار محصول')
    final_price = models.IntegerField(verbose_name='قیمت نهایی', null=True, blank=True)

    def __str__(self):
        return f"{self.product.product_name}  - {self.discount}% {self.start_time} {self.end_time}"

    class Meta:
        verbose_name = 'تخفیف مدت دار'
        verbose_name_plural = 'تخفیف های مدت دار'

    @property
    def days_remaining(self):
        if self.end_time:
            today = jdatetime.date.today()
            delta = self.end_time - today
            return max(delta.days, 0)
        return None

    def get_product_img(self):
        if self.product.product_cover:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.product.product_cover)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_product_img.short_description = ''
    get_product_img.allow_tags = True


@receiver(pre_save, sender=ProductTimingDiscount)
def set_final_price(sender, instance, **kwargs):
    if instance.start_time and instance.day_count:
        instance.end_time = instance.start_time + jdatetime.timedelta(days=instance.day_count)

    product_inventory = instance.product_inventory
    if product_inventory:
        product_sales_price = product_inventory.product_sales_price
        if product_sales_price:
            instance.final_price = product_sales_price * (1 - instance.discount / 100)

class ProductGallery(models.Model):
    image = models.ImageField(upload_to='marketplace/products/galleries/', verbose_name='تصویر')
    alt_image = models.CharField(max_length=255, verbose_name='متن جایگزین')
    title_image = models.CharField(max_length=255, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='galleries',
                                       verbose_name='محصول')

    def get_image(self):
        if self.product.product_cover:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.product.product_cover)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_image.short_description = ''
    get_image.allow_tags = True

    class Meta:
        verbose_name = 'گالری محصول فروشگاه'
        verbose_name_plural = 'گالری محصولات فروشگاه'

    def __str__(self):
        return f'{self.product}'

class ProductStatus(models.Model):
    rate = models.IntegerField(default=0, verbose_name='امتیاز')
    like = models.IntegerField(default=0, verbose_name='پسند شد')
    dis_like = models.IntegerField(default=0, verbose_name='پسند نشد')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_status',
                                       verbose_name='محصول')

    class Meta:
        verbose_name = 'لایک - امتیاز محصول'
        verbose_name_plural = 'لایک ها - امتیازهای محصول'

    def get_product_img(self):
        if self.product.product_cover:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.product.product_cover)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_product_img.short_description = ''
    get_product_img.allow_tags = True

    def __str__(self):
        return f'{self.product.product_name}: rate({self.rate}) like({self.like}) dis like({self.dis_like})'

class ProductComment(models.Model):
    comment = models.TextField(verbose_name='متن نظر')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت نظر : (فعال/غیرفعال)')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='market_product_comments',
                                       verbose_name='محصول')
    created_at = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ثبت محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")

    def __str__(self):
        return f'{self.product.product_name} {self.user.user_phone}): {self.comment}'

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نضرات محصولات'

    def get_product_img(self):
        if self.product.product_cover:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.product.product_cover)
        return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_product_img.short_description = ''
    get_product_img.allow_tags = True