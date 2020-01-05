from django.contrib import admin

# Register your models here.

from product.models import Product

# 该字段负责修改文章默认显示的字段；默认只显示标题
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','id']

admin.site.register(Product) #把产品模块注册到Django admin后台并能显示