from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Swap)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(ShippingAddress)
