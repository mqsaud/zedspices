from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Define Category Model """

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categroies'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Return Category Names """
        return self.name

    def get_friendly_name(self):
        """ Return Friendly Names """
        return self.friendly_name


class Product(models.Model):
    """ Define Product Model """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.CharField(max_length=25, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    credit = models.URLField(max_length=1024)

    def __str__(self):
        return self.name


class RateAndReview(models.Model):
    """
    Model to rate and review the products
    """
    class Meta:
        ordering = ['-created_on_date']

    rate_selector = (
       (5, '5'),
       (4.5, '4.5'),
       (4, '4'),
       (3.5, '3.5'),
       (3, '3'),
       (2.5, '2.5'),
       (2, '2'),
       (1.5, '1.5'),
       (1, '1'),
       (0.5, '0.5'),
    )

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,
                                related_name='reviews',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    rating = models.FloatField(choices=rate_selector, default=3.5)
    user_review = models.TextField()
    created_on_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
