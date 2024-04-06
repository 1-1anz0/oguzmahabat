from django.contrib import admin
from products.models import *
from mptt.admin import MPTTModelAdmin

# admin.site.register(Category, MPTTModelAdmin)

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price']
    prepopulated_fields = {'slug' : ('title', )}