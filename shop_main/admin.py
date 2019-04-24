from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Test)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name','slug')
    search_fields = ('name','slug',)
admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title','text','picture',)
    list_display = ('title','text','picture','brand','category','cost')
    #list_filter= ('brand')
admin.site.register(Product, ProductAdmin)

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ('product','quantity','cost','total')
    search_fields = ('product','quantity','cost','total')
admin.site.register(CartItem,  CartItemAdmin)

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id','total')
    search_fields = ('id','total')
admin.site.register(Cart,  CartAdmin)

class PromoCodeAdmin(admin.ModelAdmin):
    model = PromoCode
    list_display = ('id','title','total')
    search_fields = ('title','total')
admin.site.register(PromoCode,  PromoCodeAdmin)
