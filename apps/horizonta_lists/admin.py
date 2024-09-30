from django.contrib import admin
from .models import ProductList, CategoryList, CategoryListItem, ProductListItem
from easy_select2 import select2_modelform
from django.db.models.aggregates import Count

ProductListForm = select2_modelform(ProductList, attrs={'width': '150px'})
CategoryListForm = select2_modelform(CategoryList, attrs={'width': '150px'})
CategoryListItemForm = select2_modelform(CategoryListItem, attrs={'width': '150px'})
ProductListItemForm = select2_modelform(ProductListItem, attrs={'width': '150px'})


# region Product List
class ProductListItemInstanceAdminInline(admin.TabularInline):
    model = ProductListItem
    form = ProductListItemForm
    extra = 1


@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('title', 'list_location', 'is_active', 'list_items_count', 'auto_play')
    list_editable = ('is_active',)
    inlines = [ProductListItemInstanceAdminInline]
    form = ProductListForm

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListAdmin, self).get_queryset(*args, **kwargs)
        qs = qs.annotate(items=Count('product_list_item'))
        return qs

    def list_items_count(self, obj):
        return obj.items

    list_items_count.short_description = 'تعداد آتم در لیست'


@admin.register(ProductListItem)
class ProductListItemAdmin(admin.ModelAdmin):
    list_display = ('list', 'product', 'is_active')
    list_editable = ('is_active',)
    form = ProductListItemForm


# endregion


# region Category List
class CategoryListItemInstanceAdminInline(admin.TabularInline):
    model = CategoryListItem
    form = CategoryListItemForm
    extra = 1


@admin.register(CategoryList)
class CategoryListAdmin(admin.ModelAdmin):
    list_display = ('title', 'list_location', 'is_active', 'list_items_count', 'auto_play')
    list_editable = ('is_active',)
    inlines = [CategoryListItemInstanceAdminInline]
    form = CategoryListForm

    def get_queryset(self, *args, **kwargs):
        qs = super(CategoryListAdmin, self).get_queryset(*args, **kwargs)
        qs = qs.annotate(items=Count('category_list_item'))
        return qs

    def list_items_count(self, obj):
        return obj.items

    list_items_count.short_description = 'تعداد آتم در لیست'


@admin.register(CategoryListItem)
class CategoryListItemAdmin(admin.ModelAdmin):
    list_display = ('list', 'category', 'is_active')
    list_editable = ('is_active',)
    form = CategoryListItemForm
# endregion
