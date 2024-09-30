from django.db import models
from apps.product.models import Product, Category

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


class ProductList(models.Model):
    title = models.CharField(max_length=5000, verbose_name="عنوان لیست")
    list_location = models.CharField(choices=LOCATION, max_length=500, verbose_name="محل قرار گرفتن")
    auto_play = models.BooleanField(default=False, verbose_name="شروع خودکار")
    is_active = models.BooleanField(default=True, verbose_name="وضعیت (فعال/غیرفعال)")

    def __str__(self):
        return f'{self.title} - {self.list_location}'

    def get_list_location_display_value(self):
        return self.get_list_location_display()

    class Meta:
        verbose_name = "لیست افقی محصول"
        verbose_name_plural = "لیستهای افقی محصولات"


class ProductListItem(models.Model):
    list = models.ForeignKey(to=ProductList, on_delete=models.CASCADE, related_name='product_list_item',
                             verbose_name='لیست')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='products',
                                verbose_name='محصول')
    is_active = models.BooleanField(default=True, verbose_name="وضعیت (فعال/غیرفعال)")
    link = models.URLField(blank=True, null=True, verbose_name="لینک(اختیاری)")
    title = models.CharField(max_length=5000, blank=True, null=True, verbose_name="عنوان آیتم(اختیاری)")

    def __str__(self):
        return f'{self.list}, {self.product}'

    class Meta:
        verbose_name = "آیتم لیست افقی محصول"
        verbose_name_plural = " آیتم لیست افقی محصولات"


class CategoryList(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="وضعیت (فعال/غیرفعال)")
    title = models.CharField(max_length=5000, verbose_name="عنوان لیست")
    list_location = models.CharField(choices=LOCATION, max_length=500, verbose_name="محل قرار گرفتن")
    auto_play = models.BooleanField(default=False, verbose_name="شروع خودکار")

    def __str__(self):
        return f'{self.title} - {self.list_location}'

    def get_list_location_display_value(self):
        return self.get_list_location_display()

    class Meta:
        verbose_name = "لیست افقی دسته"
        verbose_name_plural = "لیستهای افقی دسته ها"


class CategoryListItem(models.Model):
    list = models.ForeignKey(to=CategoryList, on_delete=models.CASCADE, related_name='category_list_item',
                             verbose_name='لیست')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='category',
                                 verbose_name='دسته بندی')
    is_active = models.BooleanField(default=True, verbose_name="وضعیت (فعال/غیرفعال)")
    link = models.URLField(blank=True, null=True, verbose_name="لینک(اختیاری)")
    title = models.CharField(max_length=5000, blank=True, null=True, verbose_name="عنوان آیتم(اختیاری)")

    def __str__(self):
        return f'{self.list}, {self.category}'

    class Meta:
        verbose_name = "آیتم لیست افقی دسته "
        verbose_name_plural = " آیتم لیست افقی دسته ها"
