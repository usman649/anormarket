from django.contrib import admin
from .models import Product,Category,Banner,Order,AboutUs

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','status','category',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','is_popular']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','quantity']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id','phone','email']

