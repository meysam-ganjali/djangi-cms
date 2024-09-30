from django.contrib import admin
from .models import Slider, SliderItem
from django.db.models.aggregates import Count
from easy_select2 import select2_modelform

SliderItemForm = select2_modelform(SliderItem, attrs={'width': '150px'})
SliderByProductItemForm = select2_modelform(SliderItem, attrs={'width': '150px'})


class SliderItemInstanceAdminInline(admin.StackedInline):
    model = SliderItem
    extra = 1
    form = SliderItemForm


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'register_date', 'slider_item_count', 'delay', 'is_active', 'auto_play', 'get_item')
    list_filter = ('delay', 'is_active')
    search_fields = ('title',)
    ordering = ('-register_date',)
    inlines = [SliderItemInstanceAdminInline]

    def get_queryset(self, *args, **kwargs):
        qs = super(SliderAdmin, self).get_queryset(*args, **kwargs)
        qs = qs.annotate(items_count=Count('slider_items'))
        return qs

    def slider_item_count(self, obj):
        return obj.items_count

    slider_item_count.short_description = 'تعداد اسلاید ها'


@admin.register(SliderItem)
class SliderItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_slide_img', 'link', 'is_active', 'slider', 'register_date')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('-register_date',)
    form = SliderItemForm
