from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.models import Product, Category, ProductImage, ProxyProduct


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    fields = 'image',
    extra = 0
    min_num = 0
    max_num = 3


@admin.register(ProductImage)
class ProductModelAdmin(admin.ModelAdmin):
    pass


class ProductBaseModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'is_premium', 'show_image'
    autocomplete_fields = 'category',
    inlines = [ProductImageStackedInline]

    @admin.display(description='Rasm')
    def show_image(self, obj: Product):
        first_image = obj.productimage_set.order_by('-created_at').first()
        if first_image:
            return mark_safe(f'<img src="{first_image.image.url}" width="60" height="50" />')
        return 'No Images'


@admin.register(Product)
class ProductModelAdmin(ProductBaseModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_premium=False)


@admin.register(ProxyProduct)
class ProxyProductModelAdmin(ProductBaseModelAdmin):

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_premium=True)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = 'name',
