from django.contrib import admin
from .models import WishList, WishListItems

# Register your models here.

admin.site.register(WishList)
admin.site.register(WishListItems)
