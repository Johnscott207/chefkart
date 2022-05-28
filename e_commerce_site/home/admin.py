from django.contrib import admin
from .models import Product,Cart,Product_Variant,CartItems,Order


class ProductAdmin(admin.ModelAdmin):
    pass



admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Variant, ProductAdmin)
admin.site.register(Cart,ProductAdmin)
admin.site.register(CartItems,ProductAdmin)
admin.site.register(Order,ProductAdmin)