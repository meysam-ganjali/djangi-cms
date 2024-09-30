from django.utils.html import format_html
from easy_select2 import select2_modelform
from django.contrib import admin

from apps.product.models import ProductAttribute, ProductCategory, ProductSeo, ProductTag, Product, Category, ProductInventory, ProductGallery, ProductInventoryUnit, \
    ProductTimingDiscount, ProductStatus, ProductComment
from apps.utilities import format_currency

# region select2 js
ProductAttributeForm = select2_modelform(ProductAttribute, attrs={'width': '150px'})
ProductCategoryForm = select2_modelform(ProductCategory, attrs={'width': '150px'})
ProductSeoForm = select2_modelform(ProductSeo, attrs={'width': '150px'})
ProductTagForm = select2_modelform(ProductTag, attrs={'width': '150px'})


# endregion

class ProductSeoInstanceAdminInline(admin.TabularInline):
    model = ProductSeo
    extra = 1
    form = ProductSeoForm


class ProductCategoryInstanceAdminInline(admin.TabularInline):
    model = ProductCategory
    extra = 1
    form = ProductCategoryForm


class ProductAttributeInstanceAdminInline(admin.TabularInline):
    model = ProductAttribute
    extra = 3


class ProductTagInstanceAdminInline(admin.TabularInline):
    model = ProductTag
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_logo_img', 'title', 'slug', 'parent', 'get_sub_cat')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('product', 'tag_title')
    prepopulated_fields = {"slug": ("tag_title",)}
    form = ProductTagForm


@admin.register(ProductSeo)
class ProductSeo(admin.ModelAdmin):
    list_display = ('product', 'SEO_TYPE', 'title', 'content')
    form = ProductSeoForm


class ProductInventoryInstanceAdminInline(admin.TabularInline):
    model = ProductInventory
    extra = 1
    readonly_fields = ('final_price',)


class ProductGalleryInstanceAdminInline(admin.TabularInline):
    model = ProductGallery
    extra = 3


@admin.register(ProductInventoryUnit)
class ProductInventoryUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # region action for  all Product
    def active_product(modeladmin, request, queryset):
        res = queryset.update(is_active=True)
        message = f'تعداد {res} محصول  فعال شد'
        modeladmin.message_user(request, message)

    active_product.short_description = "فعال سازی محصولات انتخابی"

    def de_active_product(modeladmin, request, queryset):
        res = queryset.update(is_active=False)
        message = f'تعداد {res}محصول  غیرفعال شد'
        modeladmin.message_user(request, message)

    de_active_product.short_description = "غیرفعال کردن محصولات انتخابی"
    # endregion

    list_display = (
        'get_product_img', 'product_name', 'created_at', 'view_count', 'is_active', 'display_inventory',
        'get_categories')
    search_fields = ('product_name', 'slug')
    ordering = ('product_name',)
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    actions = [active_product, de_active_product]
    inlines = [ProductInventoryInstanceAdminInline, ProductGalleryInstanceAdminInline, ProductCategoryInstanceAdminInline,
               ProductAttributeInstanceAdminInline,
               ProductTagInstanceAdminInline, ProductSeoInstanceAdminInline]

    def display_inventory(self, obj):
        inventories = obj.product_of_inventory.all()
        table_html = """
           <table style="width: 100%; border-collapse: collapse; text-align: center;">
               <thead>
                   <tr>
                       <th style="border: 1px solid #ddd; padding: 8px;"><small>برچسب محصول</small></th>
                       <th style="border: 1px solid #ddd; padding: 8px;"><small>قیمت فروش</small></th>
                       <th style="border: 1px solid #ddd; padding: 8px;"><small>تخفیف</small></th>
                       <th style="border: 1px solid #ddd; padding: 8px;"><small>قیمت نهایی</small></th>
                       <th style="border: 1px solid #ddd; padding: 8px;"><small>تعداد</small></th>
                       <th style="border: 1px solid #ddd; padding: 8px;"><small>واحد شمارش</small></th>
                   </tr>
               </thead>
               <tbody>
           """

        for inventory in inventories:
            table_html += f"""
               <tr>
                   <td style="border: 1px solid #ddd; padding: 8px;"><small>{inventory.product_lable}</small></td>
                   <td style="border: 1px solid #ddd; padding: 8px;"><small>{format_currency(inventory.product_sales_price)}</small></td>
                   <td style="border: 1px solid #ddd; padding: 8px;"><small>{inventory.discount_percent}%</small></td>
                   <td style="border: 1px solid #ddd; padding: 8px;"><small>{format_currency(inventory.final_price)}</small></td>
                   <td style="border: 1px solid #ddd; padding: 8px;"><small>{inventory.quantity}</small></td>
                   <td style="border: 1px solid #ddd; padding: 8px;"><small>{inventory.get_unit()}</small></td>
               </tr>
               """

        table_html += """
               </tbody>
           </table>
           """

        return format_html(table_html)

    display_inventory.short_description = 'جزئیات انبار'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.prefetch_related('product_of_inventory')
        return qs


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'get_product_img', 'product', 'quantity', 'product_sales_price_formater', 'discount_percent',
        'final_price_formater', 'get_produtc_name', 'product_lable', 'unit')

    def get_produtc_name(self, obj):
        return obj.product.product_name

    def product_sales_price_formater(self, obj):
        return format_currency(obj.product_sales_price)

    product_sales_price_formater.short_description = 'قیمت فروش'

    def final_price_formater(self, obj):
        return format_currency(obj.final_price)

    final_price_formater.short_description = 'قیمت نهایی'


@admin.register(ProductTimingDiscount)
class ProductTimingDiscountAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_time', 'day_count', 'end_time', 'discount', 'product_inventory')
    readonly_fields = ('end_time',)

@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ('product','get_product_img', 'rate', 'like', 'dis_like')

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('get_product_img', 'user', 'comment', 'is_active', 'product', 'created_at')
    list_editable = ('is_active',)

@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_image', 'alt_image', 'title_image')