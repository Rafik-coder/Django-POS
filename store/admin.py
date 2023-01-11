from django.contrib import admin
from .models import Employee, Category, Products

# Register your models here.


class CategoryTabular(admin.ModelAdmin):
    list_display = ('name', 'description')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'password', 'gender', 'salary', )
    search_fields = ['name']
    # pass


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category_id', 'stock', 'expiry_date', )
    # inlines = [CategoryTabular]
    search_fields = ['name']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Category, CategoryTabular)
admin.site.register(Products, ProductsAdmin)
