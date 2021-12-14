from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, RateAndReview
from .forms import ProductForm, RateForm
from wishlist.models import WishList


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't \
                    enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    print(product)
    wishlist = WishList.objects.get(user=request.user)
    form = RateForm()
    context = {
        'product': product,
        'form': form,
        'wishlist': wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add product to store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, Only the authorized persons \
            are allowed to perform this task')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in store
    """
    sorry_msg = 'Sorry, Only the authorized persons \
        are allowed to perform this task'
    if not request.user.is_superuser:
        messages.error(request, sorry_msg)
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing { product.name }')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def confirm_delete(request, product_id):
    """ View to return about page"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/confirm_delete.html', context)


@login_required
def delete_product(request, product_id):
    """
     Delete Product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, Only the authorized persons \
            are allowed to perform this task')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required()
def submit_review(request, product_id):
    """
    Registered user can post views about the products
    """

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RateForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                messages.success(request,
                                 'Your reviews are successfully posted.')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Unable to post your reviews ')
    context = {
        'form': form
    }

    return render(request, context)


@login_required
def edit_review(request, review_id):
    """
    A registered user can edit his own review.
    """

    review = get_object_or_404(RateAndReview, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = RateForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reviews has successfully edited')
        else:
            messages.error(request, 'Oops! Fail to edit the review. Try again')

    else:
        form = RateForm(instance=review)

    messages.info(request, 'You are editing your reviews')
    template = 'products/product_detail.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }
    return render(request, template, context)
