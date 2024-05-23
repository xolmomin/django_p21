from django.contrib import admin

from apps.models import Product, Category, Member


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price'
    search_fields = 'name',
    list_editable = 'price',


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberModelAdmin(admin.ModelAdmin):
    pass
