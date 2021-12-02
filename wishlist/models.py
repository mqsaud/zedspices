"""
Model for Wishlist
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class WishList(models.Model):
    """
    This model will show all products in user wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through='WishListItems',
                                      related_name='product_wishlists')

    def __str__(self):
        """ Return user name """
        return f'WishList({self.user}) '


class WishListItems(models.Model):
    """
    This through model will establish a relation between
    WishList model and Product model.
    """
    product = models.ForeignKey(Product,
                                blank=False,
                                null=False,
                                on_delete=models.CASCADE)
    wishlist = models.ForeignKey(WishList,
                                 blank=False,
                                 null=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
