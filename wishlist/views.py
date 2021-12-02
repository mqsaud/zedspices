"""
    View to render whishlist
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import WishList


# Create your views here.


@login_required
def wishlist(request):
    """
        User wishlist view
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_product_to_wishlist(request, product_id):
    """
     Create  wish list and add product to the wish list
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.info(request, 'Product successfully added to your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from user whish list
    """
    wishlist = WishList.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    wishlist.products.remove(product)
    messages.info(request, "You removed a product from your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))
